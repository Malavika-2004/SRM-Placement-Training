salary = 0
for i in range(7):
    hours = int(input())
    if i == 0:  
        salary += hours * 150
    elif i == 6:  
        salary += hours * 125
    else: 
        if hours > 8:
            salary += (8 * 100) + ((hours - 8) * 115)
        else:
            salary += hours * 100
print(salary)
