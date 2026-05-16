import argparse
import contextlib
import io
import unittest
from codecrafter.modules import base64_module, rot_module, binary_module, hex_module, url_module, html_module
from codecrafter.main import (
    process_operation, cli_mode, validate_input, OperationError, OPERATIONS,
)

class TestBase64Module(unittest.TestCase):
    def test_encode_decode(self):
        original = "Hello, World!"
        encoded = base64_module.encode(original)
        self.assertEqual(base64_module.decode(encoded), original)
        self.assertEqual(base64_module.decode(base64_module.encode("")), "")

    def test_decode_invalid(self):
        with self.assertRaises(Exception):
            base64_module.decode("not_base64!!")

class TestRotModule(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual(rot_module.rot13("abcXYZ"), "nopKLM")
        self.assertEqual(rot_module.rot13(rot_module.rot13("test")), "test")

    def test_rot47(self):
        text = "Hello, World!"
        encoded = rot_module.rot47(text)
        self.assertEqual(rot_module.rot47(encoded), text)

class TestBinaryModule(unittest.TestCase):
    def test_bin_to_hex(self):
        self.assertEqual(binary_module.bin_to_hex("1010"), "A")

    def test_bin_to_hex_invalid_raises(self):
        # Was: returned "Invalid binary input" (treated as success).
        with self.assertRaises(ValueError):
            binary_module.bin_to_hex("invalid")

    def test_bin_to_decimal(self):
        self.assertEqual(binary_module.bin_to_decimal("1010"), "10")

    def test_bin_to_decimal_invalid_raises(self):
        with self.assertRaises(ValueError):
            binary_module.bin_to_decimal("invalid")

class TestHexModule(unittest.TestCase):
    def test_hex_to_string(self):
        self.assertEqual(hex_module.hex_to_string("68656c6c6f"), "hello")

    def test_hex_to_string_invalid_raises(self):
        with self.assertRaises(ValueError):
            hex_module.hex_to_string("zz")  # even length, non-hex chars

    def test_hex_strips_0x_prefix_and_spaces(self):
        self.assertEqual(hex_module.hex_to_string("0x48 65 6c 6c 6f"), "Hello")

    def test_odd_length_rejected_not_silently_padded(self):
        # Regression: "abc" used to be padded to "0abc" and decoded wrongly;
        # then returned an error string; now it raises.
        with self.assertRaises(ValueError):
            hex_module.hex_to_string("abc")

class TestUrlModule(unittest.TestCase):
    def test_encode_decode(self):
        text = "hello world!"
        encoded = url_module.encode(text)
        self.assertEqual(url_module.decode(encoded), text)

    def test_encode_plus_round_trip(self):
        text = "a b&c=d"
        encoded = url_module.encode_plus(text)
        self.assertEqual(encoded, "a+b%26c%3Dd")
        self.assertEqual(url_module.decode_plus(encoded), text)

class TestHtmlModule(unittest.TestCase):
    def test_encode_decode(self):
        text = "<div>Tom & Jerry</div>"
        encoded = html_module.encode(text)
        self.assertEqual(html_module.decode(encoded), text)

    def test_encode_minimal_leaves_quotes(self):
        # Minimal encoding escapes &, < and > but not quotes
        self.assertEqual(
            html_module.encode_minimal('<a href="x">'),
            '&lt;a href="x"&gt;',
        )

    def test_encode_extended_named_entities(self):
        # (No spaces: encode_extended maps ' ' -> &nbsp;, which is lossy.)
        result = html_module.encode_extended("©<b>")
        self.assertIn("&copy;", result)
        self.assertIn("&lt;b&gt;", result)
        # Round-trips through the standard unescape
        self.assertEqual(html_module.decode(result), "©<b>")

def _make_args(**kwargs):
    """Build an argparse.Namespace with the attributes cli_mode reads."""
    defaults = dict(encode=None, decode=None, convert=None,
                    input=None, file=None, output=None)
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


def _run_cli(**kwargs):
    """Run cli_mode with captured stdout. Returns (exit_code, stdout)."""
    args = _make_args(**kwargs)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = cli_mode(args)
    return code, buf.getvalue()


class TestProcessOperation(unittest.TestCase):
    def test_known_operations(self):
        self.assertEqual(process_operation("base64_encode", "Hello"), "SGVsbG8=")
        self.assertEqual(process_operation("base64_decode", "SGVsbG8="), "Hello")
        self.assertEqual(process_operation("rot13", "Hello"), "Uryyb")
        self.assertEqual(process_operation("hex_to_string", "48656c6c6f"), "Hello")

    def test_rot47_round_trip(self):
        self.assertEqual(
            process_operation("rot47", process_operation("rot47", "Hello")),
            "Hello",
        )

    def test_unknown_operation_raises(self):
        with self.assertRaises(OperationError):
            process_operation("does_not_exist", "x")

    def test_failure_raises_operation_error(self):
        with self.assertRaises(OperationError):
            process_operation("base64_decode", "!!!not-base64")

    def test_invalid_binary_raises_operation_error(self):
        # Was: returned "Invalid binary input" as a fake success.
        with self.assertRaises(OperationError):
            process_operation("bin_to_hex", "invalid")

    def test_invalid_hex_raises_operation_error(self):
        with self.assertRaises(OperationError):
            process_operation("hex_to_string", "abc")

    def test_operations_table_complete(self):
        expected = {
            "base64_encode", "base64_decode", "rot13", "rot47",
            "hex_to_string", "bin_to_hex", "bin_to_decimal",
            "url_encode", "url_decode", "html_encode", "html_decode",
        }
        self.assertTrue(expected.issubset(set(OPERATIONS)))


class TestValidateInput(unittest.TestCase):
    def test_preserves_whitespace(self):
        # Regression: validate_input used to .strip(), corrupting
        # whitespace-significant input.
        self.assertEqual(validate_input("  hi  "), "  hi  ")

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            validate_input("")

    def test_rejects_too_long(self):
        with self.assertRaises(ValueError):
            validate_input("x" * 50, max_length=10)


class TestCliMode(unittest.TestCase):
    # Regression: --encode rot13/rot47 and --decode hex used to print
    # "Unknown operation" in the success colour and still exit 0.
    def test_encode_rot13(self):
        code, out = _run_cli(encode="rot13", input="Hello")
        self.assertEqual(code, 0)
        self.assertIn("ROT13 Encode: Uryyb", out)
        self.assertNotIn("Unknown operation", out)

    def test_encode_rot47(self):
        code, out = _run_cli(encode="rot47", input="Hello")
        self.assertEqual(code, 0)
        self.assertNotIn("Unknown operation", out)

    def test_decode_hex(self):
        code, out = _run_cli(decode="hex", input="48656c6c6f")
        self.assertEqual(code, 0)
        self.assertIn("HEX Decode: Hello", out)
        self.assertNotIn("Unknown operation", out)

    def test_encode_base64_still_works(self):
        code, out = _run_cli(encode="base64", input="Hello")
        self.assertEqual(code, 0)
        self.assertIn("SGVsbG8=", out)

    def test_convert_bin_to_hex(self):
        code, out = _run_cli(convert="bin-to-hex", input="1010")
        self.assertEqual(code, 0)
        self.assertIn("Bin To Hex: A", out)

    def test_failure_returns_nonzero(self):
        # Regression: a failing operation used to exit 0 in the success colour.
        code, out = _run_cli(decode="base64", input="!!!not-base64")
        self.assertEqual(code, 1)
        self.assertIn("Error", out)

    def test_invalid_binary_returns_nonzero(self):
        # Regression: --convert bin-to-hex with bad input used to print
        # "Invalid binary input" in green and exit 0.
        code, out = _run_cli(convert="bin-to-hex", input="invalid")
        self.assertEqual(code, 1)
        self.assertIn("Error", out)

    def test_invalid_hex_returns_nonzero(self):
        code, out = _run_cli(convert="hex-to-string", input="abc")
        self.assertEqual(code, 1)
        self.assertIn("Error", out)


if __name__ == "__main__":
    unittest.main() 