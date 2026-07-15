def print_receipt(name, food, quantity, price, delivery_charge):
    subtotal = quantity * price
    service_charge = subtotal * 0.05
    grand_total = subtotal + service_charge + delivery_charge

    print("\n========== RECEIPT ==========")
    print("Customer :", name)
    print("Food     :", food)
    print("Quantity :", quantity)
    print("Price    : RM", format(price, ".2f"))
    print("-----------------------------")
    print("Subtotal        : RM", format(subtotal, ".2f"))
    print("Service Charge (5%) : RM", format(service_charge, ".2f"))
    print("Delivery Charge : RM", format(delivery_charge, ".2f"))
    print("-----------------------------")
    print("TOTAL   : RM", format(grand_total, ".2f"))
    print("=============================")