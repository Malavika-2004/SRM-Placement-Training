n, smooth = map(int, input().split())

temp = n
i = 2

while i <= temp:
    while temp % i == 0:
        if i > smooth:
            print("Not a Smooth Number")
            exit()
        temp = temp // i
    
    i += 1

print("Smooth Number")
