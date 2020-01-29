n=int(input("Enter number:"))
sum1=int()
sum1=0
while n>0 or sum1>9:
    if(n==0):
        n=sum1
        sum1=0
    sum1 += (n%10)
    n=n//10
print(sum1)


#a=n%9
#print(a)
