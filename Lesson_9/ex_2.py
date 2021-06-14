class  Road(object):
    """ метод расчёта массы асфальта """

    def __init__(self, l=0, w=0):
        self.__length = 0
        self.__width = 0
        self.l = l
        self.w = w
        self.get_metod_road()

    def get_metod_road(self, weight=25, thickness=5):
        if self.l and self.w < 0:
            print("ValueError parameters entered with invalid value ")
        else:
            self.__length = self.l
            self.__width = self.w
            print(f"{self.__length} m * {self.__width} m * {weight} kg * {thickness} cm =", f"{self.__length * self.__width * weight * thickness / 1000}t")

road = Road(a, b)
