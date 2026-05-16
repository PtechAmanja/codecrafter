# modules/binary_module.py


def bin_to_hex(binary_str):
    """
    Converts a binary string to its uppercase hexadecimal representation.

    Args:
        binary_str (str): Binary string to convert (e.g., "1010")

    Returns:
        str: Hexadecimal value.

    Raises:
        ValueError: If the input is not valid binary.
    """
    try:
        decimal_value = int(binary_str.strip(), 2)
    except ValueError:
        raise ValueError("Invalid binary input") from None
    return hex(decimal_value)[2:].upper()


def bin_to_decimal(binary_str):
    """
    Converts a binary string to its decimal representation.

    Args:
        binary_str (str): Binary string to convert (e.g., "1010")

    Returns:
        str: Decimal value.

    Raises:
        ValueError: If the input is not valid binary.
    """
    try:
        decimal_value = int(binary_str.strip(), 2)
    except ValueError:
        raise ValueError("Invalid binary input") from None
    return str(decimal_value)
