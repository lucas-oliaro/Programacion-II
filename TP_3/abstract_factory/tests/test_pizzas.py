from TP_3.abstract_factory.store import PizzaStore, NYPizzaStore, ChicagoPizzaStore
from TP_3.abstract_factory.ingredients import Dough, NYPizzaStore, ChicagoPizzaStore

def test_ny_cheese_pizza_has_correct_dough():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert isinstance(pizza.dough, Dough)