"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, color: str, name: str, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed: float):
        if speed > 0:
            self.speed = speed
            print(f'Машина поехала со скоростью {speed} км/ч')
        else:
            print('Скорость должна быть больше нуля')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction: str):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        if self.speed > 0:
            print(f'Машина движется со скоростью: {self.speed} км/ч')
        elif self.speed == 0:
            print('Машина стоит на месте')
        else:
            print('Ошибка со скоростью машины')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color=color, name=name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина движется со скоростью: {self.speed} км/ч\n'
                  f'    !!! Внимание !!! Превышение скорости! Максимальная разрешенная скорость - 60 км/ч')
        elif self.speed > 0:
            print(f'Машина движется со скоростью: {self.speed} км/ч')
        elif self.speed == 0:
            print('Машина стоит на месте')
        else:
            print('Ошибка со скоростью машины')


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color=color, name=name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина движется со скоростью: {self.speed} км/ч\n'
                  f'   !!! Внимание!!! Превышение скорости! Максимальная разрешенная скорость - 40 км/ч')
        elif self.speed > 0:
            print(f'Машина движется со скоростью: {self.speed} км/ч')
        elif self.speed == 0:
            print('Машина стоит на месте')
        else:
            print('Ошибка со скоростью машины')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color=color, name=name, is_police=False)


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color=color, name=name, is_police=True)


# Создаем массив машин разных типов
cars = [
    SportCar(color="красная", name="спортивная машина"),
    TownCar(color="белая", name="городская машина"),
    WorkCar(color="черная", name="рабочая машина"),
    PoliceCar(color="синяя", name="полицейская машина")
]

# Для машины каждого типа
for car in cars:
    # Выводим атрибуты
    print('\n--------------------------------')
    print(f'Тип: {type(car)}')
    print(f'Цвет: {car.color}')
    print(f'Название: {car.name}')
    print(f'Является ли полицейской: {car.is_police}')

    # Вызываем методы
    car.go(100)
    car.turn("направо")
    car.show_speed()
    car.go(20)
    car.show_speed()
    car.stop()
    car.show_speed()
