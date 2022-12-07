import math


def circle(R):
    return round((math.pi * R ** 2), 2)


def rectangle(a, b):
    return round((a * b), 2)


def triangle(B, H):
    return round((B / 2 * H), 2)


while True:
    print("Введите: круг - 1, прямоугольник - 2 или треугольник - 3. Для выхoда из программы введите - 0")
    quest = int(input(""))
    if 1 == quest:
        R = int(input("Введите радиус круга: "))
        print(circle(R))
    elif 2 == quest:
        a = int(input("Введите первую сторону: "))
        b = int(input("Введите вторую: "))
        print(rectangle(a, b))
    elif 3 == quest:
        H = int(input("Введите высоту треугольника: "))
        B = int(input("Введите длинну основания: "))
        print(triangle(B, H))
    elif 0 == quest:
        break
