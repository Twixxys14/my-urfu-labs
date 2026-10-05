def find_digit_at_n(n):
    length = 1
    count = 9
    start = 1

    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    target_number = start + (n - 1) // length
    index_in_number = (n - 1) % length
    return str(target_number)[index_in_number]

try:
    n = int(input("Введите позицию N: "))
    if n > 0:
        print(f"Цифра на позиции {n}: {find_digit_at_n(n)}")
    else:
        print("Введите положительное число.")
except ValueError:
    print("Нужно ввести целое число.")