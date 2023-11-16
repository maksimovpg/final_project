import click
from classes_of_pizza import Margherita, Pepperoni, Hawaiian, Pizza
from decorators_init import log

PIZZA_INSTANCES: dict[str, Pizza] = {
    'pepperoni': Pepperoni(),
    'margherita': Margherita(),
    'hawaiian': Hawaiian(),
}


@click.group()
def cli():
    pass


@log('🛵 Доставлено за {}с!')
def deliver(pizza: Pizza) -> None:
    """
    Delivery pizza
    """
    pizza.deliver()


@log('🏠 Забрали за {}с!')
def pickup(pizza: Pizza) -> None:
    """
    Pick up pizza
    """
    pizza.pickup()


@log('♨️ Испекли за {}с!')
def bake(pizza: Pizza) -> None:
    """
    Bake pizza
    """
    pizza.bake()


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool) -> None:
    """
    Print the cooking time and baking time
     for the selected pizza from the menu.
    If a non-menu dish is specified, print the warning message.
    When the delivery flag is specified, it prints the delivery time.
    If the flag is not specified, print the pickup time.

    :param pizza_name: name of pizza from menu
    :param delivery: if true then print delivery time
    :return: None
    """
    if pizza_name in PIZZA_INSTANCES:
        pizza = PIZZA_INSTANCES[pizza_name]
    else:
        print('⚠️ Такого блюда нет в меню. Пожалуйста выбери другую пиццу!')
        return

    bake(pizza)

    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu() -> None:
    """
    Prints the menu of pizzas with their ingredients from dict
    :return: None
    """
    pizzas = [Margherita().dict(), Pepperoni().dict(), Hawaiian().dict()]

    for pizza in pizzas:
        for name, recipe in pizza.items():
            print(f'- {name}  : {recipe}')


if __name__ == '__main__':
    cli()
