catalog = [
    {"name": "Hammer", "price": 12.5, "stock": 10},
    {"name": "Sledge Hammer", "price": 45.0, "stock": 3},
    {"name": "Pliers", "price": 25.0, "stock": 4},
    {"name": "Drill", "price": 120.0, "stock": 2},
    {"name": "Saw", "price": 8.99, "stock": 0},
]

while True:
    choice = input("Choose (list, filter, search, exit): ").strip().lower()

    if choice == "exit":
        break

    elif choice == "list":
        for product in catalog:
            name = product["name"]
            price = product["price"]
            stock = product["stock"]

            if stock == 0:
                print(f"{name}: {price:.2f} EUR, out of stock")
            else:
                print(f"{name}: {price:.2f} EUR, {stock} left")

    elif choice == "filter":
        max_price = float(input("Max price: "))
        results = []

        for product in catalog:
            if product["price"] <= max_price and product["stock"] > 0:
                results.append(product)

        print(f"Found: {len(results)}")

        for product in results:
            print(product["name"])

    elif choice == "search":
        search_text = input("Search: ").strip().lower()
        # .strip() skida razmake sa pocetka i kraja teksta

        if search_text == "":
            print("Search text is empty")
            continue  # preskace ostatak kruga i vraca program na pocetak petlje

        found = []

        for product in catalog:
            if search_text in product["name"].strip().lower():
                found.append(product)

        if len(found) == 0:
            print("No products found")
        else:
            for product in found:
                print(product["name"])
    else:
        print("Unknown choice")

print("Bye")
