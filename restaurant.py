class Restaurant:
    """A restaurant named Luiggi's Pasta House that makes Italian dishes."""
    def __init__(self, name, cuisine):
        """Initialize name, cuisine attributes."""
        self.name = name
        self.cuisine = cuisine


    def luiggipastahouse(self):
        """Simulate the restaurant name in response to a command."""
        print(f"The name of the restaurant is {self.name}.")

    def italian(self):
        """Simulate the cuisine type in response to a command."""
        print(f"The cuisine type is {self.cuisine}.")


my_restaurant =Restaurant('Luiggis Pasta House', 'Italian dishes')
my_restaurant.luiggipastahouse()
my_restaurant.italian()


print(f"The restaurants name is {my_restaurant.name}.")
print(f"The cusine type is {my_restaurant.cuisine}.")
