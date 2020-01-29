def binary_search(list,low,high,num):
    if(high>=low):
        mid=low+(high-low)//2
        if list[mid]==num:
            return mid
        elif list[mid]>num:
            return binary_search(list,low,mid-1,num)
        else:
            return binary_search(list,mid+1,high,num)
    else:
        return -1
list=[10,20,30,40,50]
result=binary_search(list,0,len(list)-1,50)
if(result!=-1):
    print("found at position",result)
else:
    print("Not found")
            
            
    
