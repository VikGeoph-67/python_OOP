'''
Абстрактные классы
ABC - библиотека абстракбных базовых классов

'''
from abc import ABC, abstractmethod


class Shipping(ABC):
    def shipping(self,transport):
        pass

class Electrical_Apliance(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def electrical_consumption(self):
        pass

class Heater(Electrical_Apliance, Shipping):
    def __init__(self, heting):
        self.heating=heting

    def electrical_consumption(self):
        return 1500*self.heating

    def shipping(self,transport):
        self.transport=transport
        return transport

class Cooler(Electrical_Apliance):
    def __init__(self,  cooling):
        self.cooling=cooling

    def electrical_consumption(self):
        return 300*self.cooling

#e=Electrical_Apliance()

h=Heater(34)
print(h.heating, h.electrical_consumption(),h.shipping('Cargo ship'))
c=Cooler(12)
print(c.cooling,c.electrical_consumption())

