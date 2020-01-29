s="stringstringstring"
for i in range(0,len(s)):
    for j in range(0,i+1):
        if(s[i]==s[j]):
            break
    if i==j:
        print(s[i],end="")
