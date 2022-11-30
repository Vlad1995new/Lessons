from random import random
N = 10
a = []
l = int(input('Нижняя граница массива: '))
h = int(input('Верхняя граница массива: '))
for i in range(N):
    n = int(random()*(h-l)) + l
    a.append(n)
print(a)
print('Удаляемый диапазон')
l = int(input('   нижняя граница: '))
h = int(input('   верхняя граница: '))
i = 0
m = N
while i < m:
    if l <= a[i] <= h:
        del a[i]
        m -= 1
    else:
        i += 1
for i in range(m,N):
    a.append(0)
print(a)
