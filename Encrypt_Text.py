from cryptography.fernet import Fernet

from decryption import load_key

def encryptText(text):
    key = load_key()
    encoded_text = text.encode()
    f = Fernet(key)
    encrypted_text = f.encrypt(encoded_text)
    return encrypted_text

txt="da-f6-24-4b-1e-22"
print(encryptText(txt))

