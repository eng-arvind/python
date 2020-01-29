print("started")
def m1():
    print("m1() started")
    m2()
    print("m1() ended")

def m2():
    print("m2() started")
    try:
        m3()
    except:
        print("exception")
    print("m2() ended")

def m3():
    print("m3() started")
    a=70/0
    print("m3() ended")

m1()
print("ended")
