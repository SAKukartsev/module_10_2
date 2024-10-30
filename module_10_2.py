from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 100
        days = 1
        while i >= 0 + self.power:
            sleep(1)
            print(f'{self.name} сражается {days} день(дня)...,'
                  f' осталось количество воинов {i - self.power}')
            i -= self.power
            days += 1
        print(f'{self.name} одержал победу спустя {days - 1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')