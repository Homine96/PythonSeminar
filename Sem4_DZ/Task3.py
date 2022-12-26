# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n=int(input('Введите количество элементов списка \n'))
if n<=0:
    print('Error')

digits=[]
for i in range(n):
    temp=random.randint(1,10)
    digits.append(temp)
print(digits)

lists=[]
for i in digits:
    if i not in lists:
        lists.append(i)
print(lists)        