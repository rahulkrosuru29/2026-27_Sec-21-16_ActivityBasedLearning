# Weekly Electricity Consumption Calculation
units = []

for i in range(7):
    n = int(input("Enter electricity units for the day: "))
    units.append(n)

total = 0

for i in range(7):
    total = total + units[i]

print("Weekly Electricity Consumption:", total)

average = total / 7

print("Average Daily Consumption:", average)

for i in range(7):
    if units[i] > average:
        print("Day", i + 1, "has above-average consumption")