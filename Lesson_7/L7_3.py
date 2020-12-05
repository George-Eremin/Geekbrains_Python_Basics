class Cell:
    unit_amount: int

    def __init__(self, unit_amount: int):
        self.unit_amount = unit_amount
        self.__cell_raws = ''
        self.__order_counter = 0

    def __str__(self):
        return str(self.unit_amount)

    def __add__(self, other):
        return Cell(self.unit_amount + other.unit_amount)

    def __sub__(self, other):
        if self.unit_amount > other.unit_amount:
            return Cell(self.unit_amount - other.unit_amount)
        else:
            return 'Операция невозможна. Уменьшаемое должно быть больше вычитаемого'

    def __mul__(self, other):
        return Cell(self.unit_amount * other.unit_amount)

    def __truediv__(self, other):
        return Cell(self.unit_amount // other.unit_amount)

    def make_order(self, raw_size: int):
        self.__cell_raws = ''
        self.__order_counter = self.unit_amount

        while self.__order_counter > raw_size:
            self.__cell_raws += '*' * raw_size
            self.__cell_raws += '\n'
            self.__order_counter -= raw_size
        if self.__order_counter > 0:
            self.__cell_raws += '*' * self.__order_counter

        return self.__cell_raws


cell_A = Cell(15)
cell_B = Cell(12)

print(f'cell_A: {cell_A.unit_amount}')
print(f'cell_B: {cell_B.unit_amount}')
print(f'cell_A + cell_B = {cell_A + cell_B}')
print(f'cell_A - cell_B = {cell_A - cell_B}')
print(f'cell_B - cell_A = {cell_B - cell_A}')
print(f'cell_A * cell_B = {cell_A * cell_B}')
print(f'cell_A / cell_B = {cell_A / cell_B}')

print(f'\ncell_A.make_order(5) = \n{cell_A.make_order(5)}')
print(f'\ncell_B.make_order(5) = \n{cell_B.make_order(5)}')
