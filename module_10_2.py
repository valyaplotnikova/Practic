import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power, enemies_count=100, days_count=0):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_count = enemies_count
        self.days_count = days_count

    def battle(self):
        while self.enemies_count:
            self.days_count += 1
            self.enemies_count -= self.power
            print(f"{self.name} сражается {self.days_count}(дня)..., осталось {self.enemies_count} воинов.")
            time.sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()
        print(f"{self.name} одержал победу спустя {self.days_count} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
