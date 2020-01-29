s=input()
word=s.split()
for i in word:
    s=''.join(sorted(i))
    print(s,end=" ")
    
