# Student Performance Analysis
marks = [
    [80, 75, 90],
    [60, 85, 70],
    [90, 95, 85]
]

for i in range(3):
    total = 0

    for j in range(3):
        total = total + marks[i][j]

    average = total / 3

    print("Student", i+1)
    print("Total Marks:", total)
    print("Average Marks:", average)