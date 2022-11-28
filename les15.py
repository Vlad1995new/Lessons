# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться
import random
list1 = list(random.randint(1, 100) for i in range(10))
print(list1)
list1.sort()
print(list1)
list1.pop(0)
list1.pop(0)
print(list1)

