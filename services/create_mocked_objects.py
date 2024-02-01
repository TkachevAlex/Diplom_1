from unittest.mock import Mock, MagicMock

from services.generate_test_data import DataGenerator


class MockedObjects:

    def create_bun(self):
        bun = MagicMock()
        bun.get_name.return_value = DataGenerator().get_random_string()
        bun.get_price.return_value = DataGenerator().get_random_price()
        return bun

    def create_ingredient(self):
        ingredient = Mock()
        ingredient.get_type.return_value = DataGenerator().get_random_string()
        ingredient.get_name.return_value = DataGenerator().get_random_string()
        ingredient.get_price.return_value = DataGenerator().get_random_price()
        return ingredient
