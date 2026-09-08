n = int(input())
if 100 <= n <= 999:
    trend = (n // 10) % 10
    if trend % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")
