# 1. Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*).
#Примечание. Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно.

print('*'*17)
print('*','*',sep=' '*15)
print('*','*',sep=' '*15)
print('*'*17)

# 2. Напишите программу, которая считывает два целых числа aa и bb и выводит на экран квадрат суммы (a+b)^2
#  и сумму квадратов a^2+b^2 этих чисел.

a=int(input())
b=int(input())
print('Квадрат суммы', a,'и',b ,'равен',(a+b)**2) 
print('Сумма квадратов', a,'и',b ,'равна',a**2+b**2) 

# 3. Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках программирования. 
# Напишите программу, которая считывает четыре целых положительных числа a, b,c и d и выводит на экран значение выражения a^b + c^d
#  