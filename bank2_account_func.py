"""
Банк 2
Без ООП, через функции
Единственный счет
"""

account_name = ''
account_password = ''
account_balance = 0.00


def new_account(name, balance, password):
    global account_name, account_password, account_balance
    account_name, account_password, account_balance = name, password, balance


def check_password(password):
    if password != account_password:
        print('Incorrect password'.upper())
        return False
    return True


def show():
    print(f'{"----ACCOUNT INFO":-<82}')
    print(f'Name: {account_name}')
    print(f'Balance: {account_balance}')
    print(f'Password: {account_password}')
    print('-' * 82)


def get_help():
    print(f'{"|HELP|":-^82}')
    print(f'Press "b" to get the balance\n'
          f'Press "d" to make a deposit\n'
          f'Press "w" to make a withdrawal\n'
          f'Press "s" to show the account\n'
          f'Press "h" to show the account\n'
          f'\n\tPress "q "to quit\n')


def get_balance(password):
    return account_balance


def deposit(amount_to_deposit, password):
    global account_balance
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    account_balance += amount_to_deposit
    print('\nOperation was successful')
    print(f'\nYour new balance is: {account_balance}')
    return account_balance


def withdraw(amount_to_withdraw, password):
    global account_balance
    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None
    if amount_to_withdraw > account_balance:
        print('You cannot withdraw more than you have in your account!')
        return None

    account_balance -= amount_to_withdraw
    print(f'\nYour new balance is: {account_balance}')
    return account_balance


# Тело программы
new_account("Joe", 100, ' ')  # создаем аккаунт

while True:

    print(f'{"|PASSWORD CHECKING|":-^82}')
    user_password = input('Please enter the password: ')
    if user_password == 'q':
        break

    # Password checking
    if check_password(user_password):
        print(f'Greatings, {account_name}')
        while True:
            print()
            action = input('What do you want to do? ').lower()
            action = action[0]
            print()

            if action == 'q':
                break

            elif action == 's':
                show()

            elif action == 'h':
                get_help()

            elif action == 'b':
                print('Get Balance:')
                print(f'Your balance is: {account_balance:.2f}')

            elif action == 'd':
                print('Get Deposit: ')
                user_deposit_amount = int(input('Please enter amount to deposit: '))
                deposit(user_deposit_amount, user_password)

            elif action == 'w':
                print('Withdraw:')
                user_withdraw_amount = int(input('Please enter the amount to withdraw: '))
                withdraw(user_withdraw_amount, user_password)
    break

print(f'{"|GOOD BYE|":-^82}')
print('👋🏼')
