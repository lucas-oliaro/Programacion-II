# Trabajo Práctico: Patrones de Creación - Pizzería

## 1. Simple Factory (Pizzas Básicas)

**Decisión de diseño:**  
Se implementó el patrón Simple Factory para centralizar la creación de objetos `Pizza`.  
La clase `SimplePizzaFactory` recibe el tipo de pizza y retorna una instancia de la subclase correspondiente (`CheesePizza`, `PepperoniPizza`, etc.).  
Esto desacopla la lógica de creación del cliente (`PizzaStore`).

**Estructura:**
- `simple_factory/pizza.py`: Clases base y concretas de pizza.
- `simple_factory/simple_factory.py`: Implementación de la Simple Factory.
- `simple_factory/store.py`: `PizzaStore` utiliza la factory para crear pizzas.

---

## 2. Factory Method (NYPizzaStore/ChicagoPizzaStore)

**Decisión de diseño:**  
Se migró a Factory Method para permitir que cada sucursal (`NYPizzaStore`, `ChicagoPizzaStore`) defina su propia lógica de creación de pizzas, respetando las diferencias regionales.  
Cada store implementa el método `create_pizza(kind)`.

**Estructura:**
- `factory_method/store.py`: Clases `NYPizzaStore`, `ChicagoPizzaStore` heredan de `PizzaStore` y sobreescriben el método de creación.

---

## 3. Abstract Factory de Ingredientes por Región

**Decisión de diseño:**  
Se implementó el patrón Abstract Factory para encapsular familias de ingredientes según la región.  
Cada pizza recibe una fábrica de ingredientes (`NYPizzaIngredientFactory`, `ChicagoPizzaIngredientFactory`) que provee los ingredientes correctos.

**Estructura:**
- `abstract_factory/ingredients.py`: Interfaces y fábricas concretas de ingredientes.
- `abstract_factory/pizza.py`: Las pizzas usan la fábrica de ingredientes para su preparación.
- `abstract_factory/store.py`: Las stores regionales pasan la fábrica de ingredientes adecuada.

---

## 4. Tests: Flujos de Orden y Consistencia de Ingredientes

**Decisión de diseño:**  
Se implementaron tests para verificar:
- Que el flujo de orden de pizzas funciona correctamente.
- Que las pizzas creadas tienen los ingredientes correctos según la región y el tipo.

**Estructura:**
- `tests/test_simple_factory.py`: Tests para Simple Factory.
- `tests/test_factory_method.py`: Tests para Factory Method.
- test_pizzas.py: Tests para Abstract Factory y consistencia de ingredientes.

---

## Ejecución

- Para ejecutar los tests, desde la raíz del proyecto, por ejemplo:
  ```sh
  python -m factory.tests.test_simple_factory
  ```

---

## Resumen

Este TP muestra la evolución desde una simple fábrica de objetos hasta la abstracción completa de familias de productos, aplicando los patrones de creación para lograr flexibilidad, escalabilidad y bajo acoplamiento en el diseño de una aplicación de pizzería.