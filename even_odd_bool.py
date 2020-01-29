n=10
b=True
for i in range(0,n):
    b= not(b)
if(b):
    print("Even")
else:
    print("odd")



#"even" if not n%2 else "odd"
#"even" if not n&1 else "odd"
#"even" if (n^1)&1 else "odd"
#"even" if (n//2)*2==n else "odd"
#"even" if (n|1)==n+1 else "odd"
#"even" if (n>>1)<<1 ==n else "odd"
# if(n%2) and "odd" or "even"
