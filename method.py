class A:
    print("class")
    def m():
        print("static")
    def m1(obj):
        print("object")
    def m2(objclass):
        print("class")
    @classmethod
    def m3(addrclass):
        print("hello")
'''
obj=A()
obj.m1() # A.m1()
obj.m2() # A.m2(obj)
obj.m3() # A.m3(A) '''
