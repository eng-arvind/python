import itertools
t=int(input())
for z in range(t):
    n,k,p=map(int,input().split())
    a=sorted([int(i) for i in input().split()])
    c=list(itertools.combinations(a,k))
    res=len(c)
    for i in range(len(c)):
        for x in range(len(c[i])-1,0,-1):
            if(c[i][x]-c[i][x-1])>p:
               res -=1
               break
    res %=(pow(10,9)+7)
    print(res)
