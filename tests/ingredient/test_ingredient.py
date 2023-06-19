from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ing_farinha = Ingredient("farinha")
    ing_manteiga = Ingredient("manteiga")
    ing_manteiiga = Ingredient("manteiga")

    assert ing_farinha.name == "farinha"

    assert ing_manteiga == ing_manteiiga

    assert hash(ing_manteiga) == hash(ing_manteiiga)
    assert hash(ing_farinha) != hash(ing_manteiga)

    assert repr(ing_manteiga) == "Ingredient('manteiga')"

    assert ing_manteiga.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
