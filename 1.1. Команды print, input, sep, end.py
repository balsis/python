# 1. Напишите программу, которая выводит на экран текст «Здравствуй, мир!» (без кавычек)
print('Здравствуй, мир!')

# 2. В популярном сериале «Остаться в живых» использовалась последовательность чисел 4 8 15 16 23 42, 
# которая принесла героям удачу и помогла сорвать джекпот в лотерее. Напишите программу, 
# которая выводит данную последовательность чисел с одним пробелом между ними.
print('4', '8', '15', '16', '23', '42')

# 3. Измените предыдущую программу так, чтобы каждое число последовательности 4 8 15 16 23 42 печаталось на отдельной строке.
print('4')
print('8')
print('15')
print('16')
print('23')
print('42')

# 4. Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*)
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')

# 5. На вход программе подается строка текста – имя человека. 
# Напишите программу, которая выводит на экран приветствие 
# в виде слова «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя.
name = input()
print('Привет,', name)

# 6. На вход программе подается строка текста – название футбольной команды. Напишите программу, которая повторяет ее 
# на экране со словами « - чемпион!» (без кавычек)
print(input(), '- чемпион!')

# 7. Напишите программу, которая считывает три строки по очереди, а затем выводит их в той же последовательности, каждую на отдельной строчке.
one = input()
two = input()
three = input()
print(one)
print(two)
print(three)

# 8. Напишите программу, которая считывает три строки по очереди, а затем выводит их в обратной последовательности, каждую на отдельной строчке.
one = input()
two = input()
three = input()
print(three)
print(two)
print(one)

# 9. Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек)
print('I', 'like', 'Python', sep='***', )

# 10. Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.
a = input()
b = input()
c = input()
d = input()
print(b, c, d, sep=a)

# 11. Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), после которого должна стоять запятая и пробел, 
# а затем введенное имя и восклицательный знак.
name = input()
print('Привет,', name, end='!')