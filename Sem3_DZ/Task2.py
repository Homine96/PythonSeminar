# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n=int(input('Введите количество элементов списка \n'))
numbers_list=[]
print('Заполните список')
for  i in range(n):
        a=int(input())
        numbers_list.append(a)
print(numbers_list, end=' => ')
numbers_list2=[]

for i in range(n//2):
    numbers=numbers_list[i]*numbers_list[n-1-i]
    numbers_list2.append(numbers)   
if n % 2==1:
    numbers1=numbers_list[n//2]**2
    numbers_list2.append(numbers1)
print(numbers_list2)     
















# numbers_list2=[]
# for i in range(len(numbers_list)):
#     while i < len(numbers_list)/2 and n > len(numbers_list)/2:
#         n = n - 1
#         a = numbers_list[i] * numbers_list[n]
#         numbers_list2.append(a)
#         i += 1
# print(numbers_list2)

