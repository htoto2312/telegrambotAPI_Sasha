def col(x,y):
    if x%2==y%2:
        c=1
    else:
        c=0
    return c
n,x1,y1,x2,y2=map(int,input().split())
c1=col(x1,y1)
c2=col(x2,y2)
if n<x1 or n<x2 or n<y1 or n<y2:
    print('error')
else:
    if c1==c2:
        print(1)
    else:
        print(0)