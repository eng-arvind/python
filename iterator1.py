class List_data:
    def __init__(self,data):
        self.data=data
    def __iter__(self):
        self.cur=0
        return self
    def __next__(self):
        if self.cur>= len(self.data):
            raise StopIteration("No element")
        temp = self.data[self.cur]
        self.cur += 2
        return temp
