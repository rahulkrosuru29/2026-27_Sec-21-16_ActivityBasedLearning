#Fuel Consumption Calculator
distance = float(input("Enter distance in km: "))
fuel = float(input("Enter fuel consumed in litres: "))

mileage = distance / fuel

print("Mileage:", mileage, "km/litre")

#Route Comparison

route1 = float(input("Enter Route 1 distance: "))
route2 = float(input("Enter Route 2 distance: "))

if route1 < route2:
    print("Route 1 is shorter")
elif route2 < route1:
    print("Route 2 is shorter")
else:
    print("Both routes are equal")