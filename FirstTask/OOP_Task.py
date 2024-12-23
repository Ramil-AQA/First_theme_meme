import random
import pytest


# Определение базового класса BankAccount:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'добавлена сумма {amount}')
        else:
            print(f'неккоректная сумма депозита: {amount}')

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Ошибка, недостаточно средств")
        else:
            self.__balance -= amount
            print(f"Снятие баланса, остаток на счете: {self.__balance}")

    def get_balance(self):
        print(f"Текущий баланс: {self.__balance}")


# Создание класса SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.05

    def apply_interest(self):
        self._BankAccount__balance *= self.interest_rate
        print(f"Начислен процент {self.interest_rate} сумма баланса равна: {self._BankAccount__balance}")
        # Создание класса CheckingAccount (наследуется от BankAccount):


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount
        print(f"Снятие баланса, остаток на счете: {self._BankAccount__balance}")


my_account = SavingsAccount(owner="Timur")
my_account.deposit(random.randint(100, 10000000))
my_account.get_balance()
my_account.withdraw(random.randint(10, 10000))
my_account.apply_interest()


def test_sum_deposit():
    my_account.deposit(random.randint(1, 1000))

    assert my_account._BankAccount__balance > 0
    "Ошибка, сумма  меньше нуля"


def test_sum_withdraw():
    my_account.withdraw(random.randint(10, 10000))


assert my_account._BankAccount__balance > 0
"Ошибка, сумма  меньше нуля"
