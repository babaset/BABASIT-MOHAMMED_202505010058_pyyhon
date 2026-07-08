from food_order import food_order


def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for price and quantity.")
        return

    total = food_order(price, quantity)

    if isinstance(total, str):
        print(total)
    else:
        print(f"Total Payment = RM {total:.2f}")


if __name__ == "__main__":
    main()