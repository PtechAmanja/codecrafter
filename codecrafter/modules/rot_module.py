# modules/rot_module.py

def rot13(text):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char

    return result

def rot47(text):
    """
    Applies ROT47 cipher to the input text.
    ROT47 is a derivative of ROT13 which, in addition to scrambling letters,
    also scrambles numbers and common symbols.
    
    Args:
        text (str): Input text to encode/decode
    
    Returns:
        str: ROT47 encoded/decoded text
    """
    result = ""
    
    for char in text:
        # ROT47 works on ASCII characters from 33 (!) to 126 (~)
        if 33 <= ord(char) <= 126:
            # Shift by 47 positions in the printable ASCII range
            shifted = ((ord(char) - 33 + 47) % 94) + 33
            result += chr(shifted)
        else:
            # Keep non-printable characters unchanged
            result += char
    
    return result
