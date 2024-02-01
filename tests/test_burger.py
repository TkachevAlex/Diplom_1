from burger import Burger
from services.create_mocked_objects import MockedObjects


class TestBurger:

    def test__set_buns__mocked_bun__is_added(self):
        burger = Burger()
        burger.set_buns(MockedObjects().create_bun())
        assert burger.bun

    def test__add_ingredient__mocked_ingredient__is_added(self):
        burger = Burger()
        burger.add_ingredient(MockedObjects().create_ingredient())
        assert burger.ingredients

    def test__remove_ingredient__mocked_ingredient__is_removed(self):
        burger = Burger()
        burger.add_ingredient(MockedObjects().create_ingredient())
        burger.remove_ingredient(0)
        assert not burger.ingredients

    def test__move_ingredient__mocked_ingredient__is_moved(self):
        burger = Burger()
        for _ in range(0, 2):
            burger.add_ingredient(MockedObjects().create_ingredient())
        first_ingredient = burger.ingredients[0]
        second_ingredient = burger.ingredients[1]
        burger.move_ingredient(0, 1)
        assert first_ingredient == burger.ingredients[1] and second_ingredient == burger.ingredients[0]

    def test__get_price__mocked_bun_and_ingredient__expected_price(self):
        burger = Burger()
        bun = MockedObjects().create_bun()
        ingredient = MockedObjects().create_ingredient()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == bun.get_price() * 2 + ingredient.get_price()

    def test__get_receipt__mocked_bun_and_ingredient__expected_receipt(self):
        burger = Burger()
        bun = MockedObjects().create_bun()
        ingredient = MockedObjects().create_ingredient()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert (bun.get_name() in receipt) and (ingredient.get_name() in receipt) and (str(burger.get_price()) in receipt)

