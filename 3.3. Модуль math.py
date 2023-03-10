# 1. На плоскости евклидово расстояние между двумя точками (x1, y1) и (x2, y2) определяется p=sqrt((x1-x2)^2+(y1-y2)^2)
# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
# На вход программе подается четыре вещественных числа, каждое на отдельной строке –
# Программа должна вывести одно число – евклидово расстояние.

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(p)

# 2. Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R
# На вход программе подается одно вещественное число R
# Программа должна вывести два числа – площадь круга и длину окружности радиуса

import math

R = float(input())
C = 2 * math.pi * R
S = math.pi * R**2
print(S)
print(C)

# 3. На вход программе подается два вещественных числа a,b, каждое на отдельной строке.
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.


a, b = float(input()), float(input())
print((a + b) / 2)
print((a * b) ** 0.5)
print(2 * a * b / (a + b))
print(((a**2 + b**2) / 2) ** 0.5)

# 4. Напишите программу, вычисляющую значение тригонометрического выражения sin x + cos x + (tan x)^2 по заданному числу градусов x
# На вход программе подается одно вещественное число x измеряемое в градусах​.
# Программа должна вывести одно число – значение тригонометрического выражения.

x = float(input())
import math

r = x * math.pi / 180
print(math.sin(r) + math.cos(r) + (math.tan(r) ** 2))

# 5. Напишите программу, вычисляющую значение суммы потолка и пола числа.
# На вход программе подается одно вещественное число x
# Программа должна вывести одно число – значение указанного выражения.

from math import *

a = float(input())
print(ceil(a) + floor(a))

# 6. Даны три вещественных числа a,b,c. Напишите программу, которая находит вещественные корни квадратного уравнения ax^2+bx+c=0
# На вход программе подается три вещественных числа a,b,c, каждое на отдельной строке.
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
#  Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

from math import *

a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4 * a * c
if d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
else:
    print("Нет корней")

# 7. Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
# Площадь правильного многоугольника с длиной стороны a и количеством сторон n.
# S = (n * a^2) / (4 * tan(pi/n)). Напишите программу, которая находит площадь указанного правильного многоугольника.
# На вход программе подается два числа n и a, каждое на отдельной строке.
# Программа должна вывести вещественное число – площадь многоугольника.

from math import *

n, a = float(input()), float(input())
s = (n * a**2) / (4 * tan(pi / n))
print(s)
