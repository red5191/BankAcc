class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposite(self, add):
        self.__balance += add
        print(f'Счет пополнен на {add} MNT')

    def withdraw(self, remove):
        self.__balance -= remove
        print(f'Со счета списано {remove} MNT')

    def check_balance(self):
        print(f'Баланс по счету составляет {self.__balance} MNT')

myacc = BankAccount()

myacc.deposite(15000)
myacc.withdraw(4567)
myacc.check_balance()
