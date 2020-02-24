from landing_ship import LandingShip

ship = LandingShip(100)
print("Посадка начинается!")
while ship.height > 0:
    print(f"Высота корабля: {round(ship.height, 3)}, скорость корабля: {round(ship.speed, 2)}")
    ship.run_engine(float(input("Сколько процентов топлива вы хотите использовать?\n> ")))
    ship.move()
print(f"Корабль приземлился на скорости {round(ship.speed, 2)}")
