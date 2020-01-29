s=input()
digit=str()
count=0
even=str()
odd=str()
for i in s:
    if i.isalpha():
        continue
    elif i.isdigit():
        digit += i
    else:
        count +=1
if count%2==0:
    for i in digit:
        if int(i)%2==0:
            even += i
        else:
            odd += i
    k1=0
    k2=0
    for i in range(0,len(digit)):
        if i%2==0:
            print(even[k1],end="")
            k1 +=1
        else:
            print(odd[k2],end="")
            k2 +=1
else:
    for i in digit:
        if int(i)%2==0:
            even += i
        else:
            odd += i
    k1=0
    k2=0
    for i in range(0,len(digit)):
        if i%2!=0:
            print(even[k1],end="")
            k1 +=1
        else:
            print(odd[k2],end="")
            k2 +=1

    
            
