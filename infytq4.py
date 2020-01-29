s=input()
digit=str()
for i in s:
    if i.isalpha():
        continue
    elif i.isdigit():
        digit += i
    else:
        continue
list=set()
for i in digit:
    list.add(int(i))
list1=sorted(list,reverse=True)
if list1[len(list1)-1]%2!=0:
    for i in list1:
        print(i,end="")
else:
    for i in range(len(list1)-2,0):
        if int(list1[i])%2==0:
            t=list1[i]
            list1[i]=list1[len(list1)-1]
            list1[len(list1)-1]=t
    for i in list1:
        print(i,end="")
