# Задана целочисленная матрица, состоящая из N строк и M столбцов.
# Необходимо обойти элементы этой матрицы слева направо снизу вверх и вывести элементы именно в таком порядке в виде таблицы.
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В
# каждой из последующих N строк записаны M целых чисел – элементы матрицы.

n, m = map(int, input().split())
matr = []

for t in range(n):
    matr.append(list(map(int, input().split())))

for i in range(n - 1, -1, -1):
    for j in range(m):
        print(matr[i][j], end=' ')
    print()
