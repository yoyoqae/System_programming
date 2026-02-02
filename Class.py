class Sportsman:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name_and_speed(self):
        print("Имя:", self.name)
        print("Скорость:", self.speed)

    def run(self):
        if self.speed > 4 and self.speed < 50:
            print(f"{self.name} бежит со скоростью: {self.speed} км/ч")

        elif self.speed < 4 and self.speed > 0:
            print(f"{self.name} идет со скоростью: {self.speed} км/ч")

    def sing(self):
        if self.speed < 4 and self.speed > 0:
            print(f"{self.name} поёт")
        else:
            print(f"{self.name} не может петь, его скорость движения {self.speed} не позволяет сделать это")



sportsman1 = Sportsman("Глеб", 1)
sportsman1.get_name_and_speed()
sportsman1.run()
sportsman1.sing()

print()

sportsman2 = Sportsman("Безымянный", 5)
sportsman2.get_name_and_speed()
sportsman2.run()
sportsman2.sing()

print()

sportsman3 = Sportsman("Миша", 7)
sportsman3.get_name_and_speed()
sportsman3.run()
sportsman3.sing()
