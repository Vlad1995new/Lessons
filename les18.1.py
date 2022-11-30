import random
set1 = ()
set2 = []
n = int(input("Введите колличество множеств: "))
for i in range(n):
    set1 = {random.randint(1, 50) for j in range(10)}
    print(i+1, '. ', set1)
    set2.append(set1)
print(set2)
set3 = []
for i in set2:
    for j in i:
        if j % 3 == 0 and j not in set2[0]:
            set3.append(j)
print(set3)