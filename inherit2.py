class A:
    def __init__(self):
        print("A class")
class B(A):
    def __init__(self):
        A.__init__(self)
        print("B class")
        
