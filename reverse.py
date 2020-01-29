  
def rWord(input):
    inp=input.split(" ")
    string=' '.join(inp[::-1]) 
    string.split(" ")
    inp=' '.join(string[::-1])
    return inp
    
   
input =input()
print (rWord(input) )
