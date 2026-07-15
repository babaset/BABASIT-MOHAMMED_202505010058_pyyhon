from customer import get_customer
from receipt import print_receipt


def main():
    name, food, quantity, price, delivery_charge = get_customer()

    print_receipt(name, food, quantity, price, delivery_charge)


if __name__ == "__main__":
    main()