print("SMART PARKING FEE MANAGEMENT")

name = input("Enter customer name: ")
vehicle = input("Enter vehicle number: ")

hours = int(input("Enter parking hours: "))

if hours <= 2:
    fee = 20
elif hours <= 5:
    fee = 50
else:
    fee = 100

print("\n----- PARKING BILL -----")
print("Customer Name:", name)
print("Vehicle Number:", vehicle)
print("Parking Hours:", hours)
print("Total Parking Fee: Rs.", fee)

print("Thank you for using our parking service!")