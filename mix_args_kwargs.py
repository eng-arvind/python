def sum(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
sum(1,2)
sum(1,2,3,4,5,name="manga")
sum(1,2,name="Arvind",id=123)
sum(1,2,name="Arvind",marks=94.5)
sum(1,2,name="Arvind",marks=95.4)
