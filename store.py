from products import Product


class Store:
    """
    Represents a store that manages a collection of products.  
    """

    def __init__(self, product_list: list[Product] | None = None):
        """
        Initialize the store with an optional list of products. If no list is provided, 
        the store starts with an empty inventory.  
        """
        self.items = list(product_list) if product_list is not None else []


    def add_product(self, product):
        """
        Add a product to the store's inventory.

        Args:
            product: An instance of the Product class.

        Raises:
            TypeError: If product is not an instance of Product.
        """
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product")
        self.items.append(product)


    def remove_product(self, product):
        """
        Remove a product from the store's inventory.

        Args:
            product: An instance of the Product class.

        Raises:
            TypeError: If product is not an instance of Product.
            ValueError: If product is not found in the inventory.
        """
        if not isinstance(product, Product):
            raise TypeError("product must be an instance of Product")
        try:
            self.items.remove(product)
        except ValueError:
            raise ValueError("Product not found in the store's inventory")

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.

        Returns:
            Total quantity of all products.
        """
        return sum(product.get_quantity() for product in self.items)
    

    def get_all_products(self) -> list[Product]:
        """
        Get a list of all active products in the store.

        Returns:
            List of all active products.
        """

        return [product for product in self.items if product.is_active()]


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Process an order based on a shopping list.

        Args:
            shopping_list: A list of tuples, each containing a Product instance and the quantity to buy.

        Returns:
            The total price of the order.
        """

        total_price = 0.0

        # 1. Determine the total quantities per product (if a product appears more than once in the list)
        requested_quantities: dict[Product, int] = {}
        
        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("Each item must be a tuple of (Product, int)")
            product, quantity = item
            if not isinstance(product, Product) or not isinstance(quantity, int) or isinstance(quantity, bool):
                raise TypeError("Each item must be a tuple of (Product, int)")
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
                
            requested_quantities[product] = requested_quantities.get(product, 0) + quantity

        # 2. Check if all products are active and have enough stock
        for product, total_qty in requested_quantities.items():
            if not product.is_active():
                raise Exception(f"Product {product.name} is not active.")
            if total_qty > product.get_quantity():
                raise ValueError(f"Not enough stock for {product.name}.")

        # 3. Now purchase safely (nothing can go wrong here)
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
            
        return total_price


def main():
    """
    Main function to demonstrate the functionality of the Store and Product classes."""
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                     Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                     Product("Google Pixel 7", price=500, quantity=250),
                    ]
 
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    # erstes Produkt 1 mal kaufen, zweites Produkt 2 mal kaufen
    print(best_buy.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    # Main entry point for the Store class demonstration.
    main()  

