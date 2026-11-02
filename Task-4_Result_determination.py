# Result Determination based on Marks
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student Passed")
else:
    print("Student Failed")

total = m1 + m2 + m3
print("Total Marks:", total)

average = total / 3
print("Average:", average)

if average >= 75:
    print("Distinction")
elif average >= 60:
    print("First Class")
elif average >= 35:
    print("Pass")
else:
    print("Fail")