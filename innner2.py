print("Started")
def sample():
    a=10
    print("Sample started")
    print("sample ended")
def display(a):
    print("Display started")
    a()
    print("display ended")
display(sample)
print("Ended")
