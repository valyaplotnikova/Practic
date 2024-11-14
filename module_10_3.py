import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.deposit_done = False

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.condition:
                if self.balance + amount < 500:
                    self.balance += amount
                    print(f'Пополнение: {amount}. Баланс: {self.balance}')
                    self.condition.notify_all()

                else:
                    print(f'Запрос на пополнение {amount} отклонён, баланс превышен')

            time.sleep(0.001)
        with self.condition:
            self.deposit_done = True
            self.condition.notify_all()

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.condition:
                while self.balance > amount:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                print(f"Запрос на {amount}")
                print(f'Запрос отклонён, недостаточно средств')
                if self.deposit_done:  # Проверяем, завершен ли поток deposit
                    print("Поток deposit завершен, выходим из ожидания.")
                    return  # Выходим, если deposit завершен
                self.condition.wait()

            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()


th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')
