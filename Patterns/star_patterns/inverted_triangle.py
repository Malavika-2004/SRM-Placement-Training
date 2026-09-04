n=int(input())
for row in range(n,0,-1):
    for col in range(n-row):
        print(" ",end="")
    for col in range(2*row-1):
        print("*",end="")
    print()
