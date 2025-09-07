from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    dough: str = ""
    sauce: str = ""
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="NY Style Sauce & Cheese"; self.dough = "think"; self.sauce = "tomato"; self.toppings=["Reggiano cheese"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Cheese"; self.dough = "think"; self.sauce = "tomato";self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name="NY Style Veggie Pizza"; self.dough = "think"; self.sauce = "tomato";self.toppings=["Tomatoes", "Onions", "Mushrooms", "Peppers"]

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name="NY Style Pepperoni Pizza"; self.dough = "think"; self.sauce = "tomato";self.toppings=["Sliced Pepperoni", "Onions", "Mushrooms", "Red Peppers"]  

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name="Chicago Style Veggie Pizza"; self.dough = "think"; self.sauce = "tomato";self.toppings=["Black Olives", "Spinach", "Eggplant"]

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name="Chicago Style Pepperoni Pizza"; self.dough = "think"; self.sauce = "tomato";self.toppings=["Sliced Pepperoni", "Onions", "Mushrooms", "Red Peppers"]

