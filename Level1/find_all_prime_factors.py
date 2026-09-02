n = int(input())

i = 2

while n > 1:
    count = 0

    while n % i == 0:
        count += 1
        n //= i

    if count > 0:
        print(f"{i}->{count}")

    i += 1
