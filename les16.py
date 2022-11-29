# Найти максимальный элемент диагонали матрицы.
mat = [
    [3, 8, 8],
    [4, 2, 1],
    [9, 8, 7]
]
print('Максимальный элемент первой диагонали: ')
if mat[0][0] > mat [1][1] and mat[0][0] > mat[2][2]:
    print(mat[0][0])
elif mat[1][1] > mat [0][0] and mat[1][1] > mat[2][2]:
    print(mat[1][1])
else:
    print(mat[2][2])
print('Максимальный элемент второй диагонали: ')
if mat[2][0] > mat [1][1] and mat[2][0] > mat[0][2]:
    print(mat[2][0])
elif mat[1][1] > mat [2][0] and mat[1][1] > mat[0][2]:
    print(mat[1][1])
else:
    print(mat[0][2])
