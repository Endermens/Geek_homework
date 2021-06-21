class NoZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input("введите число: "))
b = 6

try:
    if a == 0:
        raise NoZeroError("Вы поделили на ноль, теперь вселенная всхлопнеться")
except NoZeroError as err:
    print(err)
else:
    c = b/a
