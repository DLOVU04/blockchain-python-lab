TPS = [30, 160, 50000, 20, 45]
NAMES = ["Ethereum", "BSC", "Solana", "Polygon", "Arbitrum"]


def hourly_array(tps):
    return [x * 3600 for x in tps]


def max_index(arr):
    best_i = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[best_i]:
            best_i = i
    return best_i, arr[best_i]


def moving_average(arr, window=3):
    return [sum(arr[i:i + window]) / window for i in range(len(arr) - window + 1)]


def frequencies(pairs):
    result = {}
    for key, value in pairs:
        result[key] = result.get(key, 0) + value
    return result


def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def run():
    print("1) Массив транзакций/час:")
    for name, value in zip(NAMES, hourly_array(TPS)):
        print(f"   {name}: {value:,}")

    idx, value = max_index(TPS)
    print(f"\n2) Максимум в массиве: {value} (индекс {idx}, {NAMES[idx]})")

    print("\n3) Скользящее среднее TPS (окно 3):")
    for v in moving_average(TPS):
        print(f"   {v:.2f}")

    log = [("uniswap", 7000), ("aave", 5000), ("uniswap", 5500),
           ("compound", 4500), ("aave", 3500)]
    print("\n4) Частоты по массиву пар:")
    for k, v in frequencies(log).items():
        print(f"   {k}: {v:,}")

    arr = [1, 2, 3, 4, 5]
    print(f"\n5) Реверс массива на месте: {reverse_in_place(arr)}")


if __name__ == "__main__":
    run()