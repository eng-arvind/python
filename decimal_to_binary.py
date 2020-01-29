n=int(input("Enter decimal number:"))
sum=0
a=1
while(n>0):
    r=n%2
    sum += r*a
    n=n//2
    a *= 10
print(sum)
