n=int(input())
for row in range(1,2*n):
    for col in range(1,2*n):
        if row==col or (row+col)==2*n:
            print("*",end="")
        else:
            print(" ",end="")
    print()        
