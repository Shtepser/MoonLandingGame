from landing_ship import LandingShip


class Game:

    SAFE_SPEED = 5

    def __init__(self, height):
        self.start_height = height
        self.ship = LandingShip(self.start_height)

    def ask_fuel(self):
        while True:
            request = float(input("Сколько процентов топлива вы хотите использовать?\n> "))
            if request >= self.ship.fuel:
                print("Невозможно! В баках осталось только {round(self.ship.fuel, 2)}% топлива")
                continue
            return request

    def play(self):
        print("Посадка начинается!")
        while self.ship.height > 0:
            print(self.ship.get_status())
            self.ship.run_engine(self.ask_fuel())
            self.ship.move()
        print(f"Корабль приземлился на скорости {round(self.ship.speed, 2)}")
        if abs(self.ship.speed) > Game.SAFE_SPEED:
            print("Корабль разбился")
        else:
            print("Корабль совершил мягкую посадку")
