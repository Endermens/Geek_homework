import random
import time

class Car(object):
    """ car state """
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        s_1 = "stop"
        s_2 = "go"
        s_3 = "turn"
        self.engine = [s_1, s_2]
        self.status = [s_1, s_2, s_3]
        self.limitation = 60
        self.chec_status()

    def chec_status(self):
        if self.name == "TownCar":
            self.limitation = 60
        if self.name == "WorkCar":
            self.limitation = 40
        if self.name == "PoliceCar":
            self.limitation = 900


        a = random.randrange(1, 3)
        # return self.engine[a]
        print(a)
        if a == 1:
            self.stop()
        elif a == 2:
            self.go()

    def stop(self):
        print("car is out of order")

    def go(self):
        if self.speed > 140:
            print("your car cannot produce more than 140 km per hour, speed set to 140\n")
            self.speed = 140
        print(f"{self.name} went {self.speed} \n")
        print(self.limitation)
        if self.speed > self.limitation:
            self.is_police = True
            print("Polise status:", self.is_police)
            self.next()
        else:
            self.nice_day()


    def next(self):
        a = random.randrange(1, len(self.status))
        if a == 1:
            print("engine stalled")
            time.sleep(2)
            print("you were fined/n")
        elif a == 2:
            print("you decided not to stop")
            time.sleep(2)
            print("you were arest!/n")
        elif a == 3:
            print("you turn the corner abruptly")
            time.sleep(2)
            print("you managed to hide around the bend/n")


    def nice_day(self):
        print("you went well for donuts")



class TownCar(Car):
    """ Town Car """

class WorkCar(Car):
    """ Town Car """

class SportCar(Car):
     """ SportCar """

class PoliceCar(Car):
    """ Polise car """






bibi = TownCar(60, "red", "TownCar")
worc_c = WorkCar(30, "red", "WorkCar")
sport_c = SportCar(600, "red", "SportCar")
polise_c = PoliceCar(600, "red", "PoliceCar")
