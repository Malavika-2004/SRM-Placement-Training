n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()
