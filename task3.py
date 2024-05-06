def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Перемістити n-1 дисків з початкового стрижня на допоміжний стрижень
        hanoi(n-1, source, auxiliary, target)
        # Перемістити останній диск з початкового стрижня на цільовий стрижень
        print(f"Перемістити диск з {source} на {target}: {n}")
        # Перемістити n-1 дисків з допоміжного стрижня на цільовий стрижень
        hanoi(n-1, auxiliary, target, source)

def main():
    n = int(input("Введіть кількість дисків: "))
    source = 'A'
    target = 'C'
    auxiliary = 'B'
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    hanoi(n, source, target, auxiliary)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()