a=int(input("Enter first value"))
b=int(input("Enter second value"))
c=int(input("Enter third value"))
d=int(input("Enter fourth value"))
l=int()
s=int()
if(a>b):
    l=a
    s=b
if(c>s):
    if(c>l):
        s=l
        l=c
    else:
        s=c
if(d>s):
    if(d>l):
        s=l
        l=d
    else:
        s=d

print(s)
