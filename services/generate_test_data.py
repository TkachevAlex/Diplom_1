import random
import string

from data.data import Data


class DataGenerator:
    def get_random_string(self) -> str:
        letters = string.ascii_lowercase
        string_length = random.randint(1, 256)
        random_string = ''.join(random.choice(letters) for i in range(string_length))
        return str(random_string)

    def get_random_price(self) -> float:
        random_float = round(random.uniform(0, 999), 2)
        return random_float

    def get_random_ingredient(self) -> str:
        return random.choice(Data.ingredients)

    def get_random_type(self) -> str:
        return random.choice(Data.types)