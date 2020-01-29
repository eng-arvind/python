n=int(input())
for i in  range(1,n+1):
    for j in range((i*(i+1))//2,(i*(i+1))//2-i,-1):
        print(j if len(str(j))==2 else str(j) + ' ',end=" ")
    print()
