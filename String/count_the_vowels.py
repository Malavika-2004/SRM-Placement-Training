n=input()
n=n.lower()
count=0
for i in n:
    if i in "aeiouAEIOU":
        count=count+1
print(f"Number of vowels: {count}")
    
