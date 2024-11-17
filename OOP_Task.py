# Определение базового класса BankAccount:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f'добавлена сумма {amount}')
            else:
                print(f'ValueError: неккоректная сумма {amount}')

                def withdraw(self, amount):
                    if self.balance < amount:
                        print("Ошибка, недостаточно средств")
                    else:
                        self.balance -= amount
                        print(f"Снятие баланса, остаток на счете: {self.balance}")

                        def get_balance(self):
                            print(f"Текущий баланс {self.balance}")


# Создание класса SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate=0.05, balance=0):
        super().__init__(owner, balance)

        def apply_interest(self):
            self.balance *= interest_rate
            return self.balance

            # Создание класса CheckingAccount (наследуется от BankAccount):
            class CheckingAccount(BankAccount):
                def __init__(self, owner, balance=0):
                    super().__init__(owner, balance)

                def withdraw(self, amount):
                    if self.balance < amount:
                        print("Ошибка, недостаточно средств")
                    else:
                        self.balance -= amount
                        print(f"Снятие баланса, остаток на счете: {self.balance}")
