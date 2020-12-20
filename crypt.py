from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    open("key.key", "wb").write(key)

def encrypt(msg):
    key = open("key.key", "rb").read()
    return Fernet(key).encrypt(msg)

def decrypt(msg):
    key = open("key.key", "rb").read()
    return Fernet(key).decrypt(msg)


