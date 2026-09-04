n=int(input())
for row in range(1,2*n):
    for col in range(1,2*n):
        if row==1 or row==2*n-1 or col==1 or col==2*n-1 or row==col or (row+col)==2*n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
