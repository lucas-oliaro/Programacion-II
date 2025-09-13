from factory.simple_factory.simple_factory import SimplePizzaFactory
from factory.simple_factory.store import PizzaStore
from factory.simple_factory.pizza import CheesePizza, PepperoniPizza

def test_order_cheese_pizza():
    store = PizzaStore(SimplePizzaFactory())
    pizza = store.order_pizza("cheese")
    assert isinstance(pizza, CheesePizza), "No es una CheesePizza"

def test_order_pepperoni_pizza():
    store = PizzaStore(SimplePizzaFactory())
    pizza = store.order_pizza("pepperoni")
    assert isinstance(pizza, PepperoniPizza), "No es una PepperoniPizza"

def test_unknown_pizza_type():
    store = PizzaStore(SimplePizzaFactory())
    try:
        store.order_pizza("hawaiian")
        assert False, "No lanzó excepción para tipo desconocido"
    except ValueError as e:
        assert "Tipo inválido" in str(e)

if __name__ == "__main__":
    test_order_cheese_pizza()
    test_order_pepperoni_pizza()
    test_unknown_pizza_type()
    print("Todos los tests pasaron.")