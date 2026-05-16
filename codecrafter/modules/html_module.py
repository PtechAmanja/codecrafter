import html


def encode(text):
    """
    Encodes a string by converting special characters to HTML entities.

    Args:
        text (str): Input string to HTML encode.

    Returns:
        str: HTML-encoded string.
    """
    return html.escape(text, quote=True)


def decode(encoded_text):
    """
    Decodes HTML entities back to their original characters.

    Args:
        encoded_text (str): HTML-encoded string to decode.

    Returns:
        str: Decoded string.
    """
    return html.unescape(encoded_text)


def encode_minimal(text):
    """
    Encodes only the most essential HTML characters (&, <, >).

    Args:
        text (str): Input string to encode.

    Returns:
        str: HTML-encoded string (minimal encoding).
    """
    return html.escape(text, quote=False)


# Additional HTML entity mappings for extended encoding
EXTENDED_HTML_ENTITIES = {
    ' ': '&nbsp;',
    '¡': '&iexcl;',
    '¢': '&cent;',
    '£': '&pound;',
    '¤': '&curren;',
    '¥': '&yen;',
    '¦': '&brvbar;',
    '§': '&sect;',
    '¨': '&uml;',
    '©': '&copy;',
    'ª': '&ordf;',
    '«': '&laquo;',
    '¬': '&not;',
    '®': '&reg;',
    '¯': '&macr;',
    '°': '&deg;',
    '±': '&plusmn;',
    '²': '&sup2;',
    '³': '&sup3;',
    '´': '&acute;',
    'µ': '&micro;',
    '¶': '&para;',
    '·': '&middot;',
    '¸': '&cedil;',
    '¹': '&sup1;',
    'º': '&ordm;',
    '»': '&raquo;',
    '¼': '&frac14;',
    '½': '&frac12;',
    '¾': '&frac34;',
    '¿': '&iquest;'
}


def encode_extended(text):
    """
    Encodes text with extended HTML entities including special characters.

    Args:
        text (str): Input string to encode.

    Returns:
        str: HTML-encoded string with extended entities.
    """
    # First do basic HTML encoding
    result = html.escape(text, quote=True)

    # Then replace extended characters
    for char, entity in EXTENDED_HTML_ENTITIES.items():
        result = result.replace(char, entity)

    return result
