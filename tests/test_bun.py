import pytest

from bun import Bun
from data.data import Data
from services.generate_test_data import DataGenerator


class TestBun:

    @pytest.mark.parametrize('name', Data.buns)
    def test__get_bun_name__random_string__return_expected_name(self, name):
        price = DataGenerator().get_random_price()
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name', Data.buns)
    def test__get_bun_price__random_float__return_expected_price(self, name):
        price = DataGenerator().get_random_price()
        bun = Bun(name, price)
        assert bun.get_price() == price
