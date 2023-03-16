# 1. Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
# Программа должна вывести 10 раз текст «Python is awesome!», каждый на отдельной строке.

for i in range(10):
    print("Python is awesome!")

# 2. Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
# В первой строке записано текстовое предложение, во второй — количество повторений.
# Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.

a, n = input(), int(input())
for i in range(n):
    print(a)

# 3. Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
# Программа должна вывести указанную последовательность символов.

for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")

# 4. На вход программе подается натуральное число n.
# Напишите программу, которая печатает звездный прямоугольник размерами n x 19.
# На вход программе подаётся натуральное число n - высота звездного прямоугольника.
# Программа должна вывести звездный прямоугольник размерами n x 19.

n = int(input())
for i in range(n):
    print("*******************")

# 5. Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.
# На вход программе подается одна строка текста.
# Программа должна вывести десять строк в соответствии с условием задачи.

name = input()
for i in range(10):
    print(i, name)

# 6. На вход программе подается натуральное число n.
# Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу:
# «Квадрат числа [число] равен [число]» (без кавычек).
# На вход программе подается натуральное число n
# Программа должна вывести текст в соответствии с условием задачи.

a = int(input())
for i in range(a + 1):
    print("Квадрат числа", i, "равен", i**2)

# 7. На вход программе подается натуральное число n (n>=2) -  катет прямоугольного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.
# На вход программе подается одно натуральное число n (n>=2)
# Программа должна вывести треугольник в соответствии с условием задачи.

n = int(input())
for i in range(n):
    string = "*" * (n - i)
    print(string)

# 8. На вход программе подается три натуральных числа m, p, n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-ным днем.
# На вход программе подается три натуральных числа.
# Программа должна вывести текст в соответствии с условием задачи.

m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    sum = m * (p / 100 + 1) ** i
    print(i + 1, sum)

# 9. Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно.
# На вход программе подаются два целых числа m и n.
# Программа должна вывести числа в соответствии с условием задачи.

for i in range(int(input()), int(input()) + 1):
    print(i)

# 10. Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания, если m < n.
# В порядке убывания в противном случае.
# На вход программе подаются два целых числа m и n.
# Программа должна вывести числа в соответствии с условием задачи.

m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
elif m == n:
    print(m)

# 11. Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
# На вход программе подаются два целых числа m и n.
# Программа должна вывести числа в соответствии с условием задачи.

m, n = int(input()), int(input())
# print(m%2+m-1)
# print(n%2+n-1)
for i in range(m % 2 + m - 1, n - 1, -2):
    print(i)

# 12. Даны два целых числа m и n (m <= n).
# Напишите программу, которая выводит все числа от m до n включительно, удовлетворяющие хотя бы одному из условий:
# 1) число кратно 17;
# 2) число оканчивается на 9;
# 3) число кратно 3 и 5 одновременно.
# На вход программе подаются два натуральных числа m и n, каждое на отдельной строке.
# Программа должна вывести числа в соответствии с условием задачи.

m, n = int(input()), int(input())
for i in range(m, n + 1, 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)

# 13. Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.
# На вход программе подается натуральное число.
# Программа должна вывести таблицу умножения на введенное число.

n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
