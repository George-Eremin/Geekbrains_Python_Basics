"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def mass_calculate(self, weight=25, thickness=5):
        return self._length * self._width * weight * thickness / 1000


my_road = Road(5000, 20)
print(f'Масса асфальта = {my_road.mass_calculate(weight=25, thickness=5)} тонн')
