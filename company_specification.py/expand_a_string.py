word=input()
result=""
l=len(word)
i=0
while (i<l):
    result=result+(word[i]*int(word[i+1]))
    i=i+2
print(result)
