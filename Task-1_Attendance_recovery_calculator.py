#Attendance recovery calculator
total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

attendance = (attended / total_classes) * 100

print("Attendance:", attendance, "%")

if attendance >= 75:
    print("Attendance is sufficient")
else:
    print("Attendance is below 75%")

    required = (0.75 * total_classes - attended) / 0.25
    print("Extra classes required:", int(required) + 1)