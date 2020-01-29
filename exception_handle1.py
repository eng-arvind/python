print("started")
try:
    print("try started")
    b=1/0
    print("try ended")
except IndexError:
    print("indexerror")
except ZeroDivisionError:
    print("ZeroDivisionError")

    
