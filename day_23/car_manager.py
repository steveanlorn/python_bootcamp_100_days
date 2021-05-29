import cars
import random


class CarManager:
    def __init__(self, start_x, min_y, max_y, step):
        self.car_lines = []
        self.cars = []
        for i in range(min_y, max_y + 1, step):
            coordinate = (start_x, i)
            self.car_lines.append(coordinate)

    def deploy_car(self):
        rand_choice = random.randint(1, 6)
        if rand_choice == 1:
            line = random.choice(self.car_lines)
            self.cars.append(cars.Car(line))

    def move_cars(self, speed):
        for car in self.cars:
            car.move(speed)

    def is_hit_player(self, player):
        for car in self.cars:
            if car.distance(player.position()) < 20:
                return True
        return False
