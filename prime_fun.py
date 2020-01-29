def isprime(value):
    c=0
    for i in range(1,value+1):
        if(value%i==0):
            c += 1
    if(c==2):
        return "Prime"
    else:
        return "Not prime"
a=int(input("Enter value:"))
print(isprime(a))
