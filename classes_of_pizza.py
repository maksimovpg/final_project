class Pizza:
    """
    Class for describing pizza sizes and their recipes.

    Attributes:
    - name (str): The name of the pizza.
    - size (str): The size of the pizza (default is 'L').
    - recipe (list[str]): List of ingredients in the pizza recipe.

    Methods:
    - add_ingredient(ingredient: str) -> None:
        Adds an ingredient to the pizza recipe.
    - dict() -> dict[str, str]:
        Returns a dictionary representing the pizza recipe.
    - deliver() -> str:
        Returns a string indicating that the pizza has been delivered.
    - bake() -> str:
        Returns a string indicating that the pizza has been baked.
    - pickup() -> str:
        Returns a string indicating that the pizza has been picked up.
    """
    def __init__(self, name: str, size: str) -> None:
        self.name = name
        self.size = size
        self.recipe: list[str] = []

    def add_ingredient(self, ingredient: str) -> None:
        self.recipe.append(ingredient)

    def dict(self) -> dict[str, str]:
        recipe_str = ', '.join(self.recipe)
        return {self.name: recipe_str}

    def deliver(self) -> str:
        return f'Pizza {self.name} been delivered'

    def bake(self) -> str:
        return f'Pizza {self.name} been baked'

    def pickup(self) -> str:
        return f'Pizza {self.name} been picked up'


class Margherita(Pizza):
    """
    Margherita type of Pizza
    """

    def __init__(self, size: str = 'L') -> None:
        super().__init__('Margherita 🧀', size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('tomatoes')


class Pepperoni(Pizza):
    """
    Pepperoni type of Pizza
    """

    def __init__(self, size: str = 'L') -> None:
        super().__init__('Pepperoni 🍕', size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('pepperoni')


class Hawaiian(Pizza):
    """
    Hawaiian type of Pizza
    """

    def __init__(self, size: str = 'L') -> None:
        super().__init__('Hawaiian 🍍', size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('chicken')
        self.add_ingredient('pineapples')
