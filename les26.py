# Найти сумму цифр числа с помощью рекурсии. 112 = 4
def sum1(n):
    if n in range(0, 10):
        return n
    else:
        return n % 10 + sum1(n // 10)


n = int(input("Введите число сумму цифр которго хотите узнать: ").replace('-', ''))
print(sum1(n))
