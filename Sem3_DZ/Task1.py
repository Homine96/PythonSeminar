# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n=int(input('Введите количество элементов списка \n'))
numbers_list=[]
print('Заполните список')
for  i in range(n):
    a=int(input())
    numbers_list.append(a)
print(numbers_list)
sum=0
for i in range(1, len(numbers_list),2):
    sum+=numbers_list[i]
print(f'Сумма элемeнтов на нечетных позициях равна {sum}')    
