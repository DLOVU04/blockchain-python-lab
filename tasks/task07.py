def is_threat(share):
    return share > 0.5


def run():
    for p in (0.3, 0.51, 0.49, 0.6):
        verdict = "УГРОЗА (атака 51%)" if is_threat(p) else "безопасно"
        print(f"Доля мощности {p:.0%}: {verdict}")