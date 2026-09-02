a,b=map(int,input().split())
count=0
while(a>=b):
    a=a-b
    count=count+1
print(count)
