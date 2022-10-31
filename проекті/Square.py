def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

a,b=map(int,input().split())

c=NOD(a,b)
print(a*b//c, a*b//c//c)

    