# Вычислить число c заданной точностью d
from decimal import Decimal
num=float(input('Введите число (Например 3.124215) : \n'))
d=input('Введите желаемую точность округления (Например 1.00 или 1.000) : \n')
number=Decimal(num)
number=number.quantize(Decimal(d))
print(f"Введенное число с заданной точностью округления будет равно = ",number)