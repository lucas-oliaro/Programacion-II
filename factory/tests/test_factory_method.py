from factory.factory_method.store import NYPizzaStore, ChicagoPizzaStore
from factory.factory_method.pizza import NYStyleCheesePizza, ChicagoStyleCheesePizza

def test_ny_cheese_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert isinstance(pizza, NYStyleCheesePizza), "No es una NYStyleCheesePizza"

def test_chicago_cheese_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("cheese")
    assert isinstance(pizza, ChicagoStyleCheesePizza), "No es una ChicagoStyleCheesePizza"


if __name__ == "__main__":
    test_ny_cheese_pizza()
    test_chicago_cheese_pizza()
    print("Todos los tests de Factory Method pasaron.")