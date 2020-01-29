n=input()
list=(n.split(","))
sum=0
sum1=str()
k1=0
k2=0
for i in range(0,len(list)):
    if(list[i]=='5'):
        k1=i
    if(list[i]=='8'):
        k2=i
for i in range(0,k1):
    sum += int(list[i])
for i in range(k2+1,len(list)):
    sum += int(list[i])
for i in range(k1,k2+1):
    sum1 += list[i]
print(sum+int(sum1))
    
        
