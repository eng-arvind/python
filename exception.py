print("started")
class AError(Exception):
    pass
a=30
if a<=10:
    raise AError("msg")
print("ended")
    
