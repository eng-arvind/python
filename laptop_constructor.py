class laptop:
    company=str()
    processor=str()
    generation=int()
    price=float()
    data=[]
    n=5
    for i in range(n):
        company=input("Enter company name")
        processor=input("Enter processor name")
        generation=int(input("Enter generation name"))
        price=float(input("Enter price"))
        obj=laptop(company,processor,generation,price)
        data.append(obj)
  
    def __init__(self,company,processor,generation,price):
        self.company=company
        self.processor=processor
        self.generation=generation
        self.price=price
    
  
        
        
    
