import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


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
