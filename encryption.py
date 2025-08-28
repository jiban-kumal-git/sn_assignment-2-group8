# encryption.py

def shift_char(c, shift):
    if c.islower():
        return chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
    elif c.isupper():
        return chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
    else:
        return c

def encrypt_text(text, shift1, shift2):
    return ''.join(shift_char(c, shift1) for c in text)

def decrypt_text(text, shift1, shift2):
    return ''.join(shift_char(c, -shift1) for c in text)

def verify_decryption(original_text, decrypted_text):
    return original_text == decrypted_text
