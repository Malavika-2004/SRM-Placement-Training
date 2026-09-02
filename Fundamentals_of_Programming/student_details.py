name = input()
age = int(input())
cgpa = float(input())
grade = input()

cgpa = int(cgpa * 100) / 100

print("Name:", name)
print("Age:", age)
print("CGPA:", f"{cgpa:.2f}")
print("Grade:", grade)
