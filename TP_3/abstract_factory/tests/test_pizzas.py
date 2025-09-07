import pytest
from TP_3.abstract_factory.store import PizzaStore, NYPizzaStore, ChicagoPizzaStore


def test_chicago_pizza_store():
    chicago_store = ChicagoPizzaStore()
    pizza = chicago_store.order_pizza("Cheese")
    assert pizza.name == "Chicago Style Cheese Pizza"
    assert pizza.dough.name == "Thick Crust Dough" 
    assert pizza.sauce.name == "Plum Tomato Sauce" 


def test_chicago_clam_pizza():
    chicago_store = ChicagoPizzaStore()
    pizza = chicago_store.order_pizza("Clam")
    assert pizza.name == "Chicago Style Clam Pizza"
    assert pizza.dough.name == "Thick Crust Dough"  
    assert pizza.sauce.name == "Plum Tomato Sauce"

def test_ny_cheese_pizza():
    ny_store = NYPizzaStore()
    pizza = ny_store.order_pizza("Cheese")
    assert pizza.name == "NY Style Cheese Pizza"
    assert pizza.dough.name == "Thin Crust Dough"  
    assert pizza.sauce.name == "Marinara Sauce"

def test_veggie_cheese_pizza():
    ny_store = NYPizzaStore()
    pizza = ny_store.order_pizza("Veggie")
    assert pizza.name == "NY Style Veggie Pizza"
    assert pizza.dough.name == "Thin Crust Dough"  
    assert pizza.sauce.name == "Marinara Sauce" 
