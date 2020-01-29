            
def nextprime(n):
    while True:
        if(isprime(n+1)):
            print(n+1)
            break
        else:
            n +=1

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
  
