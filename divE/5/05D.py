В каждой клетке прямоугольной таблицы N x M записано некоторое число. 
Изначально игрок находится в левой верхней клетке. 
За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). 
При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).
Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

N, M = map(int, input().split())
a = [[int(it) for it in input().split()] for i in range(N)]
for cln in range(M - 2, -1, -1):
    a[-1][cln] += a[-1][cln + 1]
for row in range(N - 2, -1, -1):
    a[row][-1] += a[row + 1][-1]
for row in range(N - 2, -1, -1):
    for cln in range(M - 2, -1, -1):
        a[row][cln] += min(a[row + 1][cln], a[row][cln + 1])
print(a[0][0])
