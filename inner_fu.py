print("Started")
def sample():
    a=10
    print("Sample started")
    def inner():
        print("inner started & ended")
    print("sample ended")
    return inner,a
data,data1=sample()
print(data,data1)
print("Ended")
