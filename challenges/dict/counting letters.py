# Вашей программе поступает на вход строка, вам необходимо подсчитать сколько раз встретилась каждая буква в этой строке без учета регистра,
# при этом цифры и символы пунктуации нужно пропустить. Ответ нужно сохранить в словаре, в котором ключ - буква, а значение - количество раз, сколько эта буква встретилась в строке.
# В качестве ответа нужно вывести словарь

lst = input().lower()
dct = {}

for i in lst:
    if i.isalpha():
        if i in dct:
             dct[i]+=1
        else:
            dct[i] = 1
print(dct)