# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num=int(input('Введите число: \n'))

def simpleNumbers(n):
   i = 2
   simplenum = []
   while i * i <= n:
       while n % i == 0:
           simplenum.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       simplenum.append(n)
   return simplenum

list_simple=simpleNumbers(num)   
print(list_simple)