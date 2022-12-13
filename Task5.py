# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def Distance(a1,a2,b1,b2):
    dist=((a1-a2)*(a1-a2)+(b1-b2)*(b1-b2))
    dist2=dist**(0.5)
    return dist2

x1=int(input('Координаты X1 \n'))    
y1=int(input('Координаты Y1 \n'))  
x2=int(input('Координаты X2 \n'))  
y2=int(input('Координаты Y2 \n'))  

distance=round(Distance(x1,x2,y1,y2),3)
print (distance)