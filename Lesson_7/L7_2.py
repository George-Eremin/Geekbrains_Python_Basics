from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def cloth_amount(self):
        pass


class Coat(Clothes):
    size: int

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    @property
    def cloth_amount(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    height: int

    def __init__(self, name: str, height: int):
        super().__init__(name)
        self.height = height

    @property
    def cloth_amount(self):
        return self.height * 2 + 0.3


my_coat = Coat('Осеннее пальто', 52)
my_suit = Suit('Танцевальный костюм', 5)

print(f'На "{my_coat.name}" потребуется {my_coat.cloth_amount} кв.м ткани.')
print(f'На "{my_suit.name}" потребуется {my_suit.cloth_amount} кв.м ткани.')
