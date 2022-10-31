lest,k=map(int,input().split())
k=lest-k
while k>0:
    lest=lest-2
    k=k-1
    if lest<=k:
        print(0)
    else:
        print(1)
        break
