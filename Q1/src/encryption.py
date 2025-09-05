# encryption.py

def shift_char(c, shift):
    """
    Shift a single character by the specified amount, wrapping around the alphabet.
    - Lowercase letters (a-z) wrap within lowercase.
    - Uppercase letters (A-Z) wrap within uppercase.
    - Non-alphabetic characters (e.g., numbers, punctuation) are returned unchanged.
    """
    if c.islower():
        return chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
    elif c.isupper():
        return chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
    else:
        return c   # No shift for non-letter characters

def encrypt_text(text, shift1, shift2):
    """
    Encrypt text using a simple Caesar cipher with the first shift value.
    shift1 is applied to each character; shift2 is currently unused.
    Returns the encrypted string.
    """
    return ''.join(shift_char(c, shift1) for c in text)

def decrypt_text(text, shift1, shift2):
    """
    Decrypt text by reversing the Caesar cipher shift.
    Applies the negative of shift1 to each character to restore original text.
    shift2 remains unused for now.
    """
    return ''.join(shift_char(c, -shift1) for c in text)

def verify_decryption(original_text, decrypted_text):
    """
    Verify that decrypted_text matches the original_text exactly.
    Returns True if they match, False otherwise.
    """
    return original_text == decrypted_text
