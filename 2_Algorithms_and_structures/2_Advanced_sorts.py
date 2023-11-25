# 1. Вывод бинарного представления числа
def decimal_to_binary(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return decimal_to_binary(n // 2) + (n % 2)
# 2. Умножение
def multiply(a, b):
    for i in range(b):
        a += a
    return a
# 3. Возведение в степень
def power(a, b):
    for i in range(b):
        a *= a
    return a

