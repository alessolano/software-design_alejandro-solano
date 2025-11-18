from domain.products import Beverage, Food
from domain.extras import (
    WithMilk,
    WithCinnamon,
    WithChocolateFilling,
    WithCream,
)
from domain.order import Order, OrderStatus
from domain.customer import Customer
from services.kitchen import Barista, Baker


def run_simulation() -> None:
    # Instantiate customers (observers)
    ana = Customer(name="Ana", order_ids=[])
    carlos = Customer(name="Carlos", order_ids=[])

    # Build products using Decorator
    # Ana's orders
    ana_coffee_base = Beverage("cafe")
    ana_coffee = WithCinnamon(WithMilk(ana_coffee_base))
    ana_croissant_base = Food("croissant")
    ana_croissant = WithChocolateFilling(ana_croissant_base)

    # Carlos's orders
    carlos_tea = Beverage("te verde")
    carlos_double_coffee_base = Beverage("cafe doble espresso")
    carlos_double_coffee = WithCream(carlos_double_coffee_base)

    # Create orders (subjects) and attach observers
    order1 = Order(order_id=1, customer_name="Ana", product=ana_coffee)
    order1.attach(ana)
    ana.register_order(order1.order_id)

    order2 = Order(order_id=2, customer_name="Ana", product=ana_croissant)
    order2.attach(ana)
    ana.register_order(order2.order_id)

    order3 = Order(order_id=3, customer_name="Carlos", product=carlos_tea)
    order3.attach(carlos)
    carlos.register_order(order3.order_id)

    order4 = Order(order_id=4, customer_name="Carlos", product=carlos_double_coffee)
    order4.attach(carlos)
    carlos.register_order(order4.order_id)

    # Kitchen services
    barista = Barista()
    baker = Baker()

    # Console output
    print("Cliente: Ana")
    print()

    print(f"Ordena un {ana_coffee.description()}")
    print()

    print(f"Ordena un {ana_croissant.description()}")
    print()

    print("Cliente: Carlos")
    print()

    print(f"Ordena un {carlos_tea.description()}")
    print()

    print(f"Ordena un {carlos_double_coffee.description()}")
    print()

    # Preparation and state changes
    barista.prepare(order1)
    order1.change_status(OrderStatus.READY)
    print()

    baker.prepare(order2)
    order2.change_status(OrderStatus.READY)
    print()

    barista.prepare(order3)
    order3.change_status(OrderStatus.READY)
    print()

    barista.prepare(order4)
    order4.change_status(OrderStatus.READY)
    print()

    print("[Sistema]: Se notifican los clientes cuando sus pedidos estan listos.")
