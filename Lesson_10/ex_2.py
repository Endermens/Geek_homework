from abc import ABC, abstractmethod

class Clothes:
    """ clothes """
    def __init__(self, v = 0, h = 0):
        self.v = v
        self.h = h
    @property
    @abstractmethod
    def consumption(self):
        pass

    def coat(self):
        return (self.v / 6.5 + 0.5)

    @property
    def suit(self):
        return f"{2 * self.h + 0.3}"

    # @property
    def __add__(self, other):
        """ experemental """
        # return  Clothes((self.v / 6.5 + 0.5) + (other.v / 6.5 + 0.5) + (2 * self.h + 0.3) + (other.h * self.h + 0.3))
        return  Clothes(self.v + other.v, self.h + other.h)

    def __str__(self):
        return f"Объект с параметрами ({self.v}, {self.h})"





a = Clothes(100, 5)
a2 = Clothes(20, 66)
print(a.coat())
print(a.suit)
print(f"{a + a2}\n")
