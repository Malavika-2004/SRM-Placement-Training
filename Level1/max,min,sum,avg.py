numbers = input().split()

minimum = None
maximum = None
total = 0
count = 0

for x in numbers:
    n = int(x)
    
    if n == -1:
        break
    
    if minimum is None or n < minimum:
        minimum = n
        
    if maximum is None or n > maximum:
        maximum = n
    
    total += n
    count += 1

average = total / count

print("Min =", minimum)
print("Max =", maximum)
print("Sum =", total)
print("Average = {:.6f}".format(average))
