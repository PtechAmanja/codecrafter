# modules/url_module.py

import urllib.parse


def encode(text):
    """
    Encodes a string for safe use in URLs using percent encoding.

    Args:
        text (str): Input string to URL encode.

    Returns:
        str: URL-encoded string.
    """
    return urllib.parse.quote(text, safe='')


def decode(encoded_text):
    """
    Decodes a URL-encoded string.

    Args:
        encoded_text (str): URL-encoded string to decode.

    Returns:
        str: Decoded string.
    """
    return urllib.parse.unquote(encoded_text)


def encode_plus(text):
    """
    Encodes a string for use in URL query parameters (spaces become +).

    Args:
        text (str): Input string to encode.

    Returns:
        str: URL-encoded string with + for spaces.
    """
    return urllib.parse.quote_plus(text)


def decode_plus(encoded_text):
    """
    Decodes a URL-encoded string where spaces are represented as +.

    Args:
        encoded_text (str): URL-encoded string to decode.

    Returns:
        str: Decoded string.
    """
    return urllib.parse.unquote_plus(encoded_text)
