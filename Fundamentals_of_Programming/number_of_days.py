year = int(input())
month = int(input())
if year < 1900 or year > 9999:
    print(0)
else:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("29 Days")
        else:
            print("28 Days")
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        print("31 Days")
    elif month in [4, 6, 9, 11]:
        print("30 Days")
