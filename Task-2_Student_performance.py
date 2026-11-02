# Student Performance Analysis
marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

print("Student Marks:", marks)

for i in range(1, 5):
    if marks[i] > marks[i-1]:
        print("Performance Improved")
    elif marks[i] < marks[i-1]:
        print("Performance Decreased")
    else:
        print("Performance Remained Same")