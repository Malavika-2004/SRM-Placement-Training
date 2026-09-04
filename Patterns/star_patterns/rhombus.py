n=int(input())
for row in range(n-1,-1,-1):
    for space in range(0,row):
        print(" ",end="")
    for star in range(1,n+1):
        print("*",end="")
    print()        
