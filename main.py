#!/usr/bin/env python

import os


class Item:
    name: str
    amount: int
    price: float

    def __init__(self, name, amount=0, price=0.0):
        self.name = name
        self.amount = amount
        self.price = price

    def check_stock(self, treshold):
        if self.amount <= treshold:
            return False
        else:
            return True

    def buy_item(self, amount):
        self.amount += amount

    def sell_item(self, amount):
        self.amount -= amount

    def update_price(self, price):
        self.price = price

    def __repr__(self):
        return "<Item %s>" % self.name


def menu_create_item():
    item_name = input("Enter item name: ")
    item_amount = input("Enter amount: ")
    item_price = input("Enter price: ")
    print("\n%s added." % item_name)
    return Item(item_name, item_amount, item_price)


def menu_print_title():
    os.system("clear")
    print("Stoker")
    print("A little stock manager.")
    print()
    print()
    print()
    print()


def menu_title_screen():
    menu_print_title()
    print("Choose option:")
    print("    1) Add item")
    print("    2) Check stock for item")
    print("    3) Check sales info")
    print()
    print()
    print()
    print()
    print()
    print("For exit press enter 0")
    print()


if __name__ == "__main__":

    stock: list[Item] = []

    while True:

        menu_title_screen()
        try:
            option = int(input("Op: "))
            if option not in [1, 2, 3, 0]:
                raise ValueError
        except TypeError:
            menu_print_title()
            print("Option must be number")
            print("Press Enter to continue")
            _ = input()
            continue
        except ValueError:
            menu_print_title()
            print("Unknown operation")
            print("Press Enter to continue")
            _ = input()
            continue

        if option == 0:
            exit(0)
        elif option == 1:
            menu_print_title()
            _ = input("Press Enter to continue")
        elif option == 2:
            menu_print_title()
            print("items stock")
            _ = input("Press Enter to continue")
        elif option == 3:
            menu_print_title()
            print("Sales info")
            _ = input("Press Enter to continue")
