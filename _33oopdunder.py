# dunder method
from typing import Any


class Toy:
    def __init__(self, color: str, age: int) -> None:
        self.color = color
        self.age = age


figure = Toy('red', 8)
print(figure.__str__())
print(str(figure))
print(figure)


class Toy:
    def __init__(self, color: str, age: int) -> None:
        self.color = color
        self.age = age
        self.infos = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self) -> str:
        return f'{self.color}'

    def __len__(self) -> int:
        return self.age

    def __del__(self) -> None:
        print(f'{self} deleted!')

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'{self} is called!')

    def __getitem__(self, key):
        return self.infos[key]


figure = Toy('red', 8)
print(figure)
print(len(figure))
figure()
print(figure['name'])

# can be deleted with del keyword
