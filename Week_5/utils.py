
def calculate_total(coffee, tea, sandwich):
    
    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00
   
    total = (coffee * coffee_price) + (tea * tea_price) + (sandwich * sandwich_price)
    return total

def print_receipt(name, coffee, tea, sandwich, total):
    print("\n===== RECEIPT =====")
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-------------------")
    print(f"Total = RM {total:.2f}")
