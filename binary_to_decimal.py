n=int(input("Enter binary number:"))
sum=0
a=1
while(n>0):
    r=n%10
    sum += r*a
    n=n//10
    a *= 2
print(sum)
