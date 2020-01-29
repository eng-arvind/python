  
def rWord(input):
    inputWords = input.split(" ") 
    inputWords=inputWords[::-1] 
    string= ' '.join(inputWords)  
    return string 
   
input =input()
print (rWord(input) )
