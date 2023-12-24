# Задача №1(ООП)
class Auto:

    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    def move(self):
        print("move")

    def birthday(self):
        print(self.age + 1)

    def stop(self):
        print("stop")

BMW = Auto("good brand", 2020, "Black","BMW",1221)
print(BMW.mark, BMW.brand, BMW.age)
print(Auto.move, Auto.stop)

# Задача №2(наследование)
import time
class Track(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print('Attention!')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print('Max speed is', self.max_speed)




