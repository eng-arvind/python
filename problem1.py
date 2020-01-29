def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
n=int(input())
count=0
for i in range(1,n):
    k=gcd(i,n)
    if k==1:
        count=count+1

print(count)
        
