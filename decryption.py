from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_text):
    key = load_key()
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text)
    return decrypted_text.decode()