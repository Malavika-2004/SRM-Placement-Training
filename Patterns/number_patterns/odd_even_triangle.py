n=int(input())
for row in range(1,n+1):
    if row%2==0:
        for col in range(2,2*row+1,2):
            print(col,end="")
    else:
        for col in range(1,2*row,2):
            print(col,end="")
    print()            
                
