def quantum_states(n):
    return 2 ** n


def run():
    for n in (1, 2, 8, 127):
        print(f"{n:>3} кубит(ов): {quantum_states(n):,} состояний одновременно | классика: {n} состояний")