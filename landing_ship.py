from textwrap import dedent

SHIP_WEIGHT = 10
GRAVITY = 1.68
ENGINE_POWER = 3


class LandingShip(object):
    """Ship which lands on Moon"""

    def __init__(self, start_height):
        self.height = start_height
        self.fuel = 100
        self.speed = 0

    def get_status(self):
        return dedent(f"""\
        Высота: {round(self.height, 2)}
        Вертикальная скорость: {round(self.speed, 2)} м/с
        Осталось {round(self.fuel, 2)}% топлива""")

    def move(self):
        self.height += self.speed
        self.speed -= GRAVITY * SHIP_WEIGHT

    def run_engine(self, fuel):
        self.speed += ENGINE_POWER * min(fuel, self.fuel)
        self.fuel -= fuel
