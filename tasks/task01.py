NETWORKS = {"Ethereum": 30, "Binance Smart Chain": 160, "Solana": 50000}


def throughput(networks, seconds=3600):
    return {name: tps * seconds for name, tps in networks.items()}


def leader(networks):
    return max(networks, key=networks.get)


def run():
    hourly = throughput(NETWORKS)
    for name, total in hourly.items():
        print(f"{name}: {total:,} транзакций/час")
    print(f"Лидер: {leader(hourly)}")