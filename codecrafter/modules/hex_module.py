def hex_to_string(hex_input):
    """
    Converts a hexadecimal string to its character string representation.

    Args:
        hex_input (str): Hexadecimal string to convert (with or without
            spaces / 0x prefix)

    Returns:
        str: Decoded string.

    Raises:
        ValueError: If the input is not valid, even-length hexadecimal.
    """
    # Strip spaces and an optional leading 0x/0X prefix
    cleaned_hex = hex_input.strip().replace(" ", "")
    if cleaned_hex[:2].lower() == "0x":
        cleaned_hex = cleaned_hex[2:]
    cleaned_hex = cleaned_hex.lower()

    # Odd-length input is ambiguous - reject it rather than silently
    # padding (which would corrupt the decoded bytes)
    if len(cleaned_hex) % 2 != 0:
        raise ValueError("Invalid hexadecimal input")

    try:
        return "".join(
            chr(int(cleaned_hex[i:i + 2], 16))
            for i in range(0, len(cleaned_hex), 2)
        )
    except ValueError:
        raise ValueError("Invalid hexadecimal input") from None
