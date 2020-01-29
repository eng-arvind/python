def iterator(s,l):
    for i in range(s,l,1):
        if isprime(i):
            yield i
            
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
