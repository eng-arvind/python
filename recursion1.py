def no(n):
    if(n==0):
        return
    no(n//2)
    print(n%2)
no(13)
