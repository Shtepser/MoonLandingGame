from textwrap import dedent

GRAVITY = 1.68
ENGINE_POWER = 3


class LandingShip(object):
    """Ship which lands on Moon"""

    def __init__(self, weight, start_height):
        self.weight = weight
        self.height = start_height
        self.fuel = 100
        self.speed = 0

    def get_status(self):
        return dedent(f"""\
        Высота: {round(self.height, 2)}
        Вертикальная скорость: {round(self.speed, 2)} м/с
        Осталось {round(self.fuel, 2)}% топлива""")

    def move(self):
        self.speed -= GRAVITY * self.weight
        self.height += self.speed

    def run_engine(self, fuel):
        self.speed += ENGINE_POWER * fuel
        self.fuel -= fuel
