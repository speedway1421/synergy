def sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов массива,
    расположенных строго между максимальным и минимальным элементами.

    :param arr: список целых чисел
    :return: сумма отрицательных элементов между max и min
    """
    if not arr:
        raise ValueError("Массив не должен быть пустым.")

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    left = min(max_index, min_index) + 1
    right = max(max_index, min_index)

    total = 0

    for i in range(left, right):
        if arr[i] < 0:
            total += arr[i]

    return total


def main():
    try:
        n = int(input("Введите размер массива N: "))

        if n <= 0:
            print("Размер массива должен быть положительным.")
            return

        arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

        if len(arr) != n:
            print("Количество введенных элементов не соответствует N.")
            return

        result = sum_negative_between_min_max(arr)
        print("Сумма отрицательных элементов между максимальным и минимальным:", result)

    except ValueError:
        print("Ошибка ввода. Необходимо вводить целые числа.")


if __name__ == "__main__":
    main()
