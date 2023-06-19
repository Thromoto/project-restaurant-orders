import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish_lasanha = Dish("lasanha", 70)
    dish_pizza = Dish("pizza", 50)
    dish_pizzaa = Dish("pizza", 50)

    assert dish_pizza.name != "lasanha"
    assert dish_pizza.name == "pizza"

    assert hash(dish_lasanha) != hash(dish_pizza)
    assert hash(dish_pizzaa) == hash(dish_pizza)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pizza", "asdf")
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("pizza", -5)

    assert repr(dish_pizza) == "Dish('pizza', R$50.00)"

    assert dish_pizza == dish_pizzaa

    dish_pizza.add_ingredient_dependency(Ingredient("farinha"), 10)

    assert dish_pizza.recipe == {Ingredient("farinha"): 10}
    assert dish_pizza.get_ingredients() == {Ingredient("farinha")}
    assert dish_pizza.get_ingredients() != {Ingredient("ovo")}
    assert dish_pizza.get_restrictions() == {Restriction.GLUTEN}
