name = input("Enter your name: ")

mark1 = float(input("Enter Python mark: "))
mark2 = float(input("Enter C mark: "))
mark3 = float(input("Enter Maths mark: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
