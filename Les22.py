# Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем
# Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.
from random import randint


def random1(a, b):
    global result2
    result2 = []
    for i in range(1, 10):
        i = randint(a, b)
        result2.append(i)


peremen = random1(int(input("Введите начало диапазона: ")), int(input("Введx`xите окончание диапазона: ")))
print(result2)
