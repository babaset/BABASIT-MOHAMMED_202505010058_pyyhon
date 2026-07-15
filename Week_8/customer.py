def get_customer():
    print("=== Customer Information ===")

    name = input("Customer Name: ")
    food = input("Food Ordered (Cake/Muffin): ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item (RM): "))
    delivery = input("Delivery (Y/N): ")

    if delivery.upper() == "Y":
        delivery_charge = 5.00
    else:
        delivery_charge = 0.00

    return name, food, quantity, price, delivery_charge