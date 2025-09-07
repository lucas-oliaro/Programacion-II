import pytest
from TP_3.abstract_factory.store import PizzaStore, NYPizzaStore, ChicagoPizzaStore


def test_chicago_pizza_store():
    chicago_store = ChicagoPizzaStore()
    pizza = chicago_store.order_pizza("Cheese")
    assert pizza.name == "Chicago Style Cheese Pizza"
    assert pizza.dough.name == "Thick Crust Dough" 
    assert "Plum Tomato Sauce" == pizza.sauce.name


def test_chicago_clam_pizza():
    chicago_store = ChicagoPizzaStore()
    pizza = chicago_store.order_pizza("Clam")
    assert pizza.name == "Chicago Style Clam Pizza"
    assert pizza.dough.name == "Thick Crust Dough"  
    assert "Plum Tomato Sauce" == pizza.sauce.name
