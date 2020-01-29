class citizen:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(citizen):
    def __init__(self,name,age,marks):
        citizen.__init__(self,name,age)
        self.marks=marks
        
