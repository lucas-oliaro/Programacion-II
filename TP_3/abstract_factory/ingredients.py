from abc import ABC, abstractmethod

# Ingredient products
class Dough:
    def __init__(self, name): 
        self.name = name 

    def __str__(self):
        return self.name

class Sauce:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Cheese:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Clams:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Onion:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class Mushroom:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class SlicedPepperoni:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class Ham:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...
    # Additional ingredients can be added here
    @abstractmethod
    def create_onion(self) -> Onion: ...
    @abstractmethod
    def create_mushroom(self) -> Mushroom: ...
    @abstractmethod
    def create_sliced_pepperoni(self) -> SlicedPepperoni: ...
    @abstractmethod
    def create_ham(self) -> Ham: ...


# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   return Clams("Fresh Clams")
    def create_onion(self) : return Onion("Garlic")
    def create_mushroom(self): return Mushroom("Mushrooms")
    
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   return Clams("Frozen Clams")
    def create_pepperoni(self): return SlicedPepperoni("Sliced Pepperoni")
    def create_ham(self): return Ham("Ham")
    