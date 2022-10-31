v,r,p,b=map(int,input().split())
x,y=v//b,r//p
if y>=x:
    print(x)
elif x>y:
    print(y)
