# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n=int(input('Введите количество элементов списка \n'))
digits=[]
for i in range(n):
    temp=round(random.uniform(1,20),2)
    digits.append(temp)
print(digits,end=" => ")

digits2=[]
for i in range(len(digits)):
    ls=round(digits[i]*100 % 100, 2)
    digits2.append(ls)
   
print((max(digits2)-min(digits2))/100)

