# Tuple-Based Product Catalogue Audit
products = (
    ("Pen", 10),
    ("Book", 50),
    ("Pencil", 5),
    ("Bag", 500)
)

print("Product Catalogue:")

for product in products:
    print("Name:", product[0])
    print("Price:", product[1])

print("Products costing more than 100:")

for product in products:
    if product[1] > 100:
        print(product[0])