import hashlib


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def run():
    h = sha256("blockchain")
    print(f"SHA-256('blockchain') =\n{h}")