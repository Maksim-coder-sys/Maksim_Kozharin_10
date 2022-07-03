from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,v):
        self.v = v
    def __add__(self, other):
        return round((self.v / 6.5 + 0.5) + (other.v * 2 + 0.3))
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        super().__init__(v)
    @property
    def fabric_consumption(self):
        return round(self.v/6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, v):
        super().__init__(v)
        self.v = v
    @property
    def fabric_consumption(self):
        return round(self.v * 2 + 0.3)

c = Coat(10)

s = Suit(15)

print(c.fabric_consumption)

print(s.fabric_consumption)

print(c+s)