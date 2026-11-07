import hashlib


def mine(data, difficulty):
    prefix = "0" * difficulty
    nonce = 0
    while True:
        h = hashlib.sha256(f"{data}{nonce}".encode()).hexdigest()
        if h.startswith(prefix):
            return nonce, h
        nonce += 1


def run():
    nonce, h = mine("block1", 4)
    print(f"difficulty=4, nonce={nonce}")
    print(f"hash={h}")