import math
x=float(input())
if x<=2:
    x=5*x**2-7
elif 2<x<5:
    x=1/(2*x-4)
elif x>=5:
    x=math.sqrt(x-5)

print(round(x,3))