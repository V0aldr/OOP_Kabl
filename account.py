"""
Банковский счёт через ООП
"""


class Account:
    """
    Банковский счёт
    """

    def __init__(self, name: str, balance: int = 0.00, password: str = None) -> None:
        self.name = name
        self.balance = int(balance)
        self.password = password

    def check_password(self, password):
        if password != self.password:
            print('Incorrect password'.upper())
            return False
        return True

    def get_balance(self, password):
        if self.check_password(password):
            return self.balance

    def deposit(self, amount_to_deposit, password):
        if self.check_password(password):
            if amount_to_deposit <= 0:
                print('You cannot deposit a negative amount!')
                return None
            self.balance += amount_to_deposit
            print(f'\nOperation was successful, {self.name}')
            print(f'\nYour new balance is: {self.balance}\n')
            print('-' * 82)
            return self.balance

    def withdraw(self, amount_to_withdraw, password):
        if self.check_password(password):
            if amount_to_withdraw < 0:
                print('You cannot withdraw a negative amount!')
                return None
            if amount_to_withdraw > self.balance:
                print('You cannot withdraw more than you have in your account!')
                return None

            self.balance -= amount_to_withdraw
            print(f'\nYour new balance is: {self.balance}')
            return self.balance

    # Код для отладки
    def show(self):
        print(f'{"----ACCOUNT INFO":-<82}')
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        print(f'Password: {self.password}')
        print('-' * 82)

    @staticmethod
    def get_help():
        print(f'{"|HELP|":-^82}')
        print(f'Press "b" to get the balance\n'
              f'Press "d" to make a deposit\n'
              f'Press "w" to make a withdrawal\n'
              f'Press "s" to show the account\n'
              f'Press "h" to show the account\n'
              f'\n\tPress "q "to quit\n')


a, b, c = (Account('Alex', 100, '123'),
           Account('Tonya', 100, '****'),
           Account('Masha', 100, '1111'))

assert a.balance == 100.00
assert b.balance == 100.00
assert c.balance == 100.00

info = a.show(), b.show(), c.show()
a.deposit(50, '123')
b.deposit(999.999, '****')
c.withdraw(25, '1111')
str(info)


print(f'\n\n{"END":*^82}\n')
