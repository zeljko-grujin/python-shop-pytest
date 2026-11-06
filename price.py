catalog = [
    {"name": "Hammer", "price": 12.5, "stock": 10},
    {"name": "Sledge Hammer", "price": 45.0, "stock": 3},
    {"name": "Pliers", "price": 25.0, "stock": 4},
    {"name": "Drill", "price": 120.0, "stock": 2},
    {"name": "Saw", "price": 8.99, "stock": 0},
]

search_name = input("Product: ").strip().lower()
quantity = int(input("Quantity: "))  # Kolicina

product = None

for item in catalog:
    if item["name"].lower() == search_name:
        product = item
        break

if product is None:
    print("Product not found")
elif quantity < 1:
    print("Invalid quantity")
elif quantity > product["stock"]:
    print(f"Not enough stock: only {product['stock']} left")
else:
    name = product["name"]
    price = product["price"]
    subtotal = quantity * price  # Medjuzbir

    if subtotal >= 100:
        discount_percent = 10
    elif subtotal >= 50:
        discount_percent = 5
    else:
        discount_percent = 0
    discount = subtotal * discount_percent / 100
    total = subtotal - discount

    print(f"{name}: {quantity} * {price:.2f} EUR")
    print(f"Subtotal: {subtotal:.2f} EUR")
    print(f"Discount: {discount:.2f} EUR ({discount_percent}%)")
    print(f"Total: {total:.2f} EUR")
