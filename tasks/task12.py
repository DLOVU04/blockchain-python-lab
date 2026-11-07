import hashlib


def sign(message, private_key):
    return hashlib.sha256((message + private_key).encode()).hexdigest()


def verify(message, signature, private_key):
    return sign(message, private_key) == signature


def run():
    key = "secret-key"
    msg = "transfer 10 BTC"
    sig = sign(msg, key)
    print(f"Подпись: {sig[:24]} ...")
    print(f"Проверка верной подписи: {verify(msg, sig, key)}")
    print(f"Проверка при подмене сообщения: {verify('transfer 100 BTC', sig, key)}")