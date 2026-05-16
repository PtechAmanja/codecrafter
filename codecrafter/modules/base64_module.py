import base64

def encode(text):
    """
    Encodes a string into Base64 format.

    Args:
        text (str): Input string to encode.

    Returns:
        str: Base64-encoded string.
    """
    return base64.b64encode(text.encode('utf-8')).decode('ascii')

def decode(encoded_text):
    """
    Decodes a Base64-encoded string or bytes.
    
    Args:
        encoded_text (str or bytes): Base64 data to decode.
    
    Returns:
        str: Decoded string.
    """
    if isinstance(encoded_text, str):
        encoded_text = encoded_text.encode('utf-8')
    return base64.b64decode(encoded_text).decode('utf-8')