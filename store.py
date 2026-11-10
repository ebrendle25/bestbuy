class Product:
    """
    Represents a product in the store.

    Attributes:
        name (str): Name of the product.
        price (float): Price per unit.
        quantity (int): Available stock.
        active (bool): Whether the product is active (available for sale).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Create a new product. The product is active by default.

        Args:
            name: Name of the product, must not be empty.
            price: Price per unit, must not be negative.
            quantity: Initial stock, must not be negative.

        Raises:
            TypeError: If an argument has the wrong type.
            ValueError: If the name is empty or price/quantity is negative.
        """

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty or whitespace")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current stock of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set the stock of the product. Deactivates the product if quantity is 0.

        Args:
            quantity: New stock, must not be negative.

        Raises:
            TypeError: If quantity is not an integer.
            ValueError: If quantity is negative.
        """

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a string representation of the product to the console."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Buy a given quantity of the product and update the stock.

        Args:
            quantity: Number of units to buy, must be greater than 0.

        Returns:
            The total price of the purchase.

        Raises:
            TypeError: If quantity is not an integer.
            ValueError: If quantity is not positive, exceeds the stock,
                or the product is inactive.
        """

        if not self.active:
            raise ValueError("Product is not active")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price



def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()    

if __name__ == "__main__":
    main()  
