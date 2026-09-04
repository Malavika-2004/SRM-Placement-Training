n = int(input())
for i in range(n):
    for j in range(n):
        if n % 2 == 0:
            if i == n // 2 - 1 or i == n // 2 or j == n // 2 - 1 or j == n // 2:
                print("0", end="")
            else:
                print("1", end="")
        else:
            if i == n // 2 or j == n // 2:
                print("0", end="")
            else:
                print("1", end="")
    print()
