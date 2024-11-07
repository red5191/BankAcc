class BankAccount:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, deposite, withdraw):
        try:
            if deposite > 0 and withdraw > 0:
                self.__balance += float(deposite)
                print(f'Счет пополнен на {deposite} MNT')

                self.__balance -= float(withdraw)
                print(f'Со счета было списано {withdraw} MNT')
            else:
                print('Депозит и списание должны быть положительными числами')
        except ValueError:
            print('Депозит и списание должны быть положительными числами')

    def get_balance(self):
        print(f'Баланс по счету составляет {self.__balance} MNT')

    balance = property(get_balance, set_balance)


myacc = BankAccount()

myacc.set_balance(15000, 4567)
myacc.get_balance()