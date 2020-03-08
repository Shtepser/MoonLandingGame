from textwrap import dedent

GRAVITY = 1.68


class LandingShip(object):
    """Ship which lands on Moon"""

    def __init__(self, weight, engine_power, start_height):
        self.weight = weight
        self.engine_power = engine_power
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
        if fuel < 0:
            raise ValueError("Fuel can't be negative!")
        self.speed += self.engine_power * min(fuel, self.fuel)
        self.fuel -= min(fuel, self.fuel)
