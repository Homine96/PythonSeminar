# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень числа к :  '))
if k <= 0:
    print('Error')
else:
    koef_lists = []
    for i in range(k):
        koef = random.randint(0, 10)
        koef_lists.append(koef)
    print(f'Список коэффициентов = {koef_lists}')

    znak = ['+', '-']
    # vybor_znaka=random.choice(znak)
    # print(vybor_znaka)

    result = ''
    n = k
    i = 0
    while i < n:
        a = random.choice(koef_lists)
        if not a == 0:
            vybor_znaka = random.choice(znak)
            result = result + f'{a}*x^{n - i}  '
            result = result + f'{vybor_znaka}  '
            i = i + 1
        elif a == 0:
            i = i + 1
    result = result + f'{random.choice(koef_lists)}' + ' = 0'
    print(result)
    with open("D:\education_py\PythonSeminar\Sem4_DZ\Task4.txt", "a", encoding="utf-8") as my_f:
        my_f.write(f'{result} \n')