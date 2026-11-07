import importlib


def main():
    for i in range(1, 16):
        module = importlib.import_module(f"tasks.task{i:02d}")
        print(f"\n{'=' * 60}\nЗадание {i}\n{'=' * 60}")
        module.run()


if __name__ == "__main__":
    main()