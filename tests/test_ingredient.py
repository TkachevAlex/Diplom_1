import pytest
from data.data import Data
from ingredient import Ingredient
from services.generate_test_data import DataGenerator


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', Data.types)
    def test__get_ingredient_type__random_string__return_expected_name(self, ingredient_type):
        name = DataGenerator().get_random_ingredient()
        price = DataGenerator().get_random_price()
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('name', Data.ingredients)
    def test__get_ingredient_name__random_string__return_expected_name(self, name):
        ingredient_type = DataGenerator().get_random_type()
        price = DataGenerator().get_random_price()
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    def test__get_ingredient_price__random_float__return_expected_price(self):
        ingredient_type = DataGenerator().get_random_type()
        name = DataGenerator().get_random_ingredient()
        price = DataGenerator().get_random_price()
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
