# Shopping Multi-Product Budget Check
budget = int(input("Enter your budget: "))

p1 = int(input("Enter price of Product 1: "))
p2 = int(input("Enter price of Product 2: "))
p3 = int(input("Enter price of Product 3: "))

total = p1 + p2 + p3

print("Total Shopping Amount:", total)

if total <= budget:
    print("Shopping is within budget")

else:
    print("Shopping exceeds budget")
    print("Extra Amount:", total - budget)