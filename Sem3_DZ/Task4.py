# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n=int(input('Введите число: '))
a=n
numbers=[]
while a >=1:
    x=a%2
    a=a//2
    numbers.append(x)   
numbers.reverse()
temp="".join(str(num ) for num in numbers )
print(f"Число {n} в двоичной системе -> {temp}")
