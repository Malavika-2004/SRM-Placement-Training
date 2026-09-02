n=int(input())
t=int(input())

if n%t!=0:
    print(f"The number of friends in each team is {n//t} and left out is {n%t}")
else:
    print(f"The number of friends in each team is {n//t} and left out is 0")     
