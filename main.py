from cli import deliver, bake, pickup
from classes_of_pizza import Margherita, Pepperoni, Hawaiian

if __name__ == '__main__':
    deliver(Margherita('XL'))
    bake(Pepperoni())
    pickup(Hawaiian('L'))
    print(Hawaiian().dict())
