class Stationery:
    def __init__(self, title = "Запуск отрисовки"):
        self.title = title

    def draw(self):
        """ отрисовка """
        print(f"Just start drawing! {self.title}")


class Pen(Stationery):
    """ Pen """
    def draw(self):
        print(f"Just start drawing {self.title} pen")


class Pencil(Stationery):
    """ Pencil """
    def draw(self):
        print(f"Just start drawing {self.title} pencil")

class Handle (Stationery):
    """ Handle  """
    def draw(self):
        print(f"Just start drawing {self.title} Handle ")

paper = Stationery()
paper.draw()

pencil = Pencil("DBUabdu")
pencil.draw()

pen = Pen("ssda")
pen.draw()

handle = Handle("i")
handle.draw()
