def max_dragon_power(n):
    """
    Находит максимально возможную силу стаи драконов.

    Известно общее количество голов N.
    У одного дракона может быть от 1 до 7 голов.
    Сила стаи равна произведению количества голов всех драконов.

    :param n: общее количество голов, 0 < n < 100
    :return: максимально возможная сила стаи
    """
    if n <= 0 or n >= 100:
        raise ValueError("N должно удовлетворять условию: 0 < N < 100.")

    dp = [0] * (n + 1)
    dp[0] = 1

    for total_heads in range(1, n + 1):
        best_power = 0

        for dragon_heads in range(1, min(7, total_heads) + 1):
            current_power = dragon_heads * dp[total_heads - dragon_heads]

            if current_power > best_power:
                best_power = current_power

        dp[total_heads] = best_power

    return dp[n]


def main():
    try:
        n = int(input("Введите количество голов драконьей стаи N: "))

        result = max_dragon_power(n)
        print("Максимально возможная сила стаи:", result)

    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
