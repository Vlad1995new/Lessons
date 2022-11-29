# Вычислить количество отрицательных элементов под главной диагональю матрицы.
mat = []
x = int(input('Введите колличество строк в матрице: '))
y = int(input('Введите колличество столбцов в матрице: '))
for i in range(x):
    mat1 = []
    for j in range(y):
        mat1.append(int(input('введите любое отрицательное или положительное число:')))
    mat.append(mat1)
for i in mat:
    print(i)
for i in range(x):
    for j in range(y):
        if j < i and mat[i][j] < 0:
            print(mat[i][j])


