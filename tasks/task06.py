import hashlib


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def merkle_root(txs):
    level = [sha(t) for t in txs]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        level = [sha(level[i] + level[i + 1]) for i in range(0, len(level), 2)]
    return level[0]


def run():
    txs = ["tx1", "tx2", "tx3", "tx4"]
    print(f"Merkle root: {merkle_root(txs)}")