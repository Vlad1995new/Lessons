#Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.
import random
list1 = list(random.randint(1, 100) for i in range(10))
print(list1)
a = input("Введите число a от одного до двух знаков: ")
b = input("Введите число b которое будет больше X но меньше 99: ")
len1 = 10
i = 0
x = len1
while i < x:
    if int(a) <= list1[i] <= int(b):
        del list1[i]
        x -= 1
    else:
        i += 1
for i in range(x, len1):
    list1.append(0)
print(list1)




