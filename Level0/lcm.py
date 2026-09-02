a,b = map(int,input().split())
largest = max(a, b)

while True:
    if largest % a == 0 and largest % b == 0:
        print(largest)
        break
    largest += 1
