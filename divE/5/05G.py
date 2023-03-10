Узник пытается бежать из замка, который состоит из N×M квадратных комнат, расположенных в виде прямоугольника NxM. 
Между любыми двумя соседними комнатами есть дверь, однако некоторые комнаты закрыты и попасть в них нельзя. 
В начале узник находится в левой верхней комнате и для спасения ему надо попасть в противоположную правую нижнюю комнату. 
Времени у него немного, всего он может побывать не более, чем в N+M-1 комнате на своем пути, то есть перемещаться он должен только вправо или вниз. 
Определите количество маршрутов, которые ведут к выходу.

n, m = map(int, input().split())
a = [[0 for i in range(m + 1)]]
for i in range(n):
 a.append([0] + list(map(int, input().split())))
a[0][1] = 1
for i in range(1, n + 1):
   for j in range(1, m + 1):
      if a[i][j] != 0:
       a[i][j] = a[i - 1][j] + a[i][j - 1]
if a[n][m] == 0:
  print("Impossible")
else: print(a[n][m])
