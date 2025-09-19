from factory.abstract_factory.store import NYPizzaStore, ChicagoPizzaStore

def test_ny_cheese_pizza_uses_ny_dough():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert pizza.dough.name == "Thin Crust Dough", "La pizza NY no usa Thin Crust Dough"

def test_chicago_cheese_pizza_uses_chicago_dough():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("cheese")
    assert pizza.dough.name == "Thick Crust Dough", "La pizza Chicago no usa Thick Crust Dough"

if __name__ == "__main__":
    test_ny_cheese_pizza_uses_ny_dough()
    test_chicago_cheese_pizza_uses_chicago_dough()
    print("Todos los tests de Abstract Factory pasaron.")