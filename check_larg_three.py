a=int(input("Enter first value"))
b=int(input("Enter second value"))
c=int(input("Enter third value"))
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    else:
        print(c)
else:
    print(c)
