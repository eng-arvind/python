class A:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        
class B:
    def __init__(self,e,f):
        self.e=e
        self.f=f

class C(A,B):
    print("c")
    
    
