# def decimal_to_binary(n):
#     if n == 0:
#         return ""
#     elif n > 0:
#         return decimal_to_binary(n // 2) + str(n % 2)
# n = 43
# binary = decimal_to_binary(n)
# print(f"Десятичное число {n} в двоичной системе счисления: {binary}")

# fib1 = fib2 = 1
# print(fib1, fib1, end=' ')
# n = 13
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))