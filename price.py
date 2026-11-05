name = "Hammer"
stock = 10  # Stanje magacin lupam

price = float(input("Price: "))
quantity = int(input("Quantity: "))  # Kolicina

if price <= 0:
    print("Invalid price")
elif quantity < 1:
    print("Invalid quantity")
elif quantity > stock:
    print(f"Not enough stock: only {stock} left")
else:
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
