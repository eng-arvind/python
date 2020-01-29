print("started")
def display(abc):
    print("display started")
    def inner(a,b):
        print("inner started")
        abc(a,b)
        print("inner ended")
    print("display ended")
    return inner
def sample(a,b):
    print("sample started")
    print(a,b)
    print("sample ended")
a=display(sample)
a(10,20)
print("ended")
''' *********************"output"**********************************  
started
display started
display ended
inner started
sample started
10 20
sample ended
inner ended
ended '''
