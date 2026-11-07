import hashlib


class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        raw = f"{self.index}{self.data}{self.prev_hash}"
        return hashlib.sha256(raw.encode()).hexdigest()


def build_chain(payloads):
    chain = []
    prev = "0"
    for i, data in enumerate(payloads):
        block = Block(i, data, prev)
        chain.append(block)
        prev = block.hash
    return chain


def run():
    chain = build_chain(["genesis", "tx-1", "tx-2"])
    for b in chain:
        print(f"Блок {b.index}: hash={b.hash[:16]}... prev={b.prev_hash[:16]}...")