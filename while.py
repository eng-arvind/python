c=5
while c<=10:
    print(c,end=" ")
    c +=1


c=10
print()
while c>=5:
    print(c,end=" ")
    c -=1


    
s=int(input("Enter start number:"))
l=int(input("Enter last number:"))
while s<=l:
    if(s%2==0):
        print(s,end=" ")
    s += 1
