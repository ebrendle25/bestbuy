"""Main module for the store application."""

import products
import store


def menu():
    """Print the menu and return the user's choice as an integer."""

    print(
        """
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """
    )

    return ask_number("Please choose a number (1-4): ", int, 1, 4)


def ask_number(prompt, cast, low, high):
    """Ask for a number until it is valid and within [low, high].

    The input is converted with `cast` (e.g. int or float).
    """
    while True:
        try:
            value = cast(input(prompt))
        except ValueError:
            print("Invalid input. Please choose a number.")
            continue
        if low <= value <= high:
            return value
        print(f"Value must be between {low} and {high}")


def list_products(store_obj):
    """List all products in the store."""
    for index, product in enumerate(store_obj.get_all_products(), start=1):
        print(f"{index}. {product}")


def make_order(store_obj):
    """Make an order based on user input."""
    shopping_list = []
    reserved_quantities = {}
    print("When you want to finish order, enter empty text.")
    available_products = store_obj.get_all_products()
    while True:
        product_number = input(
            "Which product # do you want? (or press Enter to finish): "
        )
        if not product_number:
            break
        try:
            product_index = int(product_number) - 1

            if product_index < 0 or product_index >= len(available_products):
                print("No products available in the store.")
                continue

            product = available_products[product_index]
        except ValueError:
            print("Invalid product number. Please try again.")
            continue

        # Calculate how much of this product is still available
        already_ordered = reserved_quantities.get(product, 0)
        remaining_stock = product.get_quantity() - already_ordered

        if remaining_stock <= 0:
            print(f"Sorry, no more {product.name} left in stock!")
            continue

        print(f"{product.name} (Available to add: {remaining_stock})")

        quantity = ask_number(
            f"What amount of {product.name} do you want? ",
            int,
            1,
            remaining_stock,
        )

        # Add it to the shopping list and save it in the dictionary
        shopping_list.append((product, quantity))
        reserved_quantities[product] = already_ordered + quantity
        print("Product added to list!\n")

    if shopping_list:
        try:
            total_price = store_obj.order(shopping_list)
            print(f"********\nOrder made! Total payment: ${total_price:.2f}\n")
        except ValueError as exc:
            print(f"Order failed: {exc}\n")
    else:
        print("No products were selected for the order.")


def start(store_obj):
    """Start the store application, allowing the user to interact with the store."""

    while True:
        choice = menu()

        if choice == 1:
            list_products(store_obj)
        elif choice == 2:
            print(f"Total of {store_obj.get_total_quantity()} items in store")
        elif choice == 3:
            print("------")
            list_products(store_obj)
            print("------")
            make_order(store_obj)
        elif choice == 4:
            print("Bye!")
            break


def main():
    """setup initial stock of inventory"""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
