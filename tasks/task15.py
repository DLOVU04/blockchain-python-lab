import itertools

GENERATIONS = [127, 433, 1121]


def growth_rates(values):
    return [b / a for a, b in itertools.pairwise(values)]


def run():
    rates = growth_rates(GENERATIONS)
    avg = sum(rates) / len(rates)
    forecast = round(GENERATIONS[-1] * avg)
    print(f"Поколения кубитов: {GENERATIONS}")
    print(f"Коэффициенты роста: [{rates[0]:.2f}, {rates[1]:.2f}]")
    print(f"Средний темп роста: x{avg:.2f}")
    print(f"Прогноз следующего поколения: ~{forecast} кубитов")