# Cоздать список длин n,значения формируются по формуле
#  3к+1 , где к принимает значения от 1 до n

n=int(input())
list=[]
for i in range(1,n+1):
    x=3*i+1
    list.append(x)
print(list)    