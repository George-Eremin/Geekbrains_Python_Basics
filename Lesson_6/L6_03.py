"""
3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker
  name: str
  surname: str
  position: str
  _income: {"wage": float, "bonus": float}
  
  def __init(self, name:str, surname: str):
    self.name = name
    self.surname = surname
    self._income = {wage: 100, bonus: 20} 

class Position(Worker)
  def get_full_name():
    return (f'{self.name} {self.surname})
  
  


