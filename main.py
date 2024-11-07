class BankAccount:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, value):
        try:
            if value + self.balance > 0:
                self.__balance += float(value)
                if value > 0:
                    print(f'Счет пополнен на {value} MNT')
                else:
                    print(f'Со счета было списано {value} MNT')
            else:
                print(f'Нельзя списать больше чем числится на счете')
        except ValueError:
            print('Депозит и списание должны быть положительными числами')

    def get_balance(self):
        return self.__balance

    balance = property(get_balance, set_balance)


myacc = BankAccount()

myacc.balance = 15000
myacc.balance = -4567
print(f'Баланс по счету составляет {myacc.balance} MNT')
