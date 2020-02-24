SHIP_WEIGHT = 10
GRAVITY = 1.68
ENGINE_POWER = 3


class LandingShip(object):
    """Ship which lands on Moon"""

    def __init__(self, start_height):
        self.height = start_height
        self.fuel = 100
        self.speed = 0

    def move(self):
        self.height += self.speed
        self.speed -= GRAVITY * SHIP_WEIGHT

    def run_engine(self, fuel):
        self.speed += ENGINE_POWER * fuel
        self.fuel -= fuel
