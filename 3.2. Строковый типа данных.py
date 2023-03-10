# 1. Напишите программу, которая выводит текст:
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

print(
    '"Python is a great language!", said Fred. "I '
    + "don't ever remember having this much fun before"
    + '."'
)

# 2. Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».
# На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.
# Программа должна вывести текст в соответствии с условием задачи.

name = input()
surname = input()
print("Hello " + name + " " + surname + "! You just delved into Python")

# 3. Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
# На вход программе подаётся строка – название футбольной команды.
# Программа должна вывести текст в соответствии с условием задачи.

a = input()
print("Футбольная команда", a, "имеет длину", len(a), "символов")

# 4. Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

a, b, c = input(), input(), input()
if len(a) == min(len(a), len(b), len(c)):
    print(a)
if len(b) == min(len(a), len(b), len(c)):
    print(b)
if len(c) == min(len(a), len(b), len(c)):
    print(c)
if len(a) == max(len(a), len(b), len(c)):
    print(a)
if len(b) == max(len(a), len(b), len(c)):
    print(b)
if len(c) == max(len(a), len(b), len(c)):
    print(c)

# 5. Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
# На вход программе подаются три строки, каждая на отдельной строке.
# Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

a = len(input())
b = len(input())
c = len(input())
if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print("YES")
else:
    print("NO")

# 6. Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
# На вход программе подается одна строка.
# Программа должна вывести текст в соответствии с условием задачи.

if "синий" in input():
    print("YES")
else:
    print("NO")

# 7. Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
# На вход программе подается одна строка.
# Программа должна вывести текст в соответствии с условием задачи.

a = input()
if "суббота" in a or "воскресенье" in a:
    print("YES")
else:
    print("NO")

# 8. Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
# На вход программе подаётся одна строка – email адрес.
# Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.
# Примечание. Наличие символов @ и . недостаточно для корректности email адреса, однако их отсутствие гарантировано влечёт за собой неверный email.

email = input()
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")
