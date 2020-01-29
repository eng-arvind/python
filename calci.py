def calci(data,a,b):
    if(data=="+"):
        return a+b
    elif(data=="-"):
        return a-b
    elif(data=="/"):
        return a/b
    elif(data=="*"):
        return a*b
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
print("Enter the operator:")
print("'+' for Addition")
print("'-' for Substraction")
print("'/' for Division")
print("'*' for Multiplication")
data=input()
print("Answer=",calci(data,a,b))
        
