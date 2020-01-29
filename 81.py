n=int(input("Enter number:"))
k=1
for i in range (0,n*2+1):
    if(i>n):
        i=i-2*k
        k +=1
    print(i%(n+1),end=" ")
