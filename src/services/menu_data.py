import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        with open(source_path, newline="") as file:
            r = csv.reader(file)
            next(r)

            for row in r:
                dish_name = row[0]
                price = float(row[1])
                ingredient_name = row[2]
                quantity = int(row[3])
                ingredient = Ingredient(ingredient_name)
                self.ingredients.add(ingredient)

                plate = next(
                    (d for d in self.dishes if d.name == dish_name),
                    None,
                )
                if plate is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)
                dish.add_ingredient_dependency(ingredient, quantity)
