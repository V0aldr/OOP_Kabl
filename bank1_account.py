"""
Без ООП
Банк. Версия 1
Единственный счет
"""

account_name = 'Alex'
account_password = '123'
account_balance = 100

while True:
    print(f'{"|HELP|":-^82}')
    print(f'Press "b" to get the balance\nPress "d" to make a deposit\n'
          f'Press "w" to make a withdrawal\nPress "s" to show the account\n'
          f'Press "q "to quit\n')
    print(f'{"|ACCOUNT|":-^82}')

    action = input('What do you want to do? ').lower()
    action = action[0]

    if action == 'q':
        break

    elif action == 'b':
        print('Get Balance:')
        user_password = input('Please enter the password: ')
        if user_password != account_password:
            print('Incorrect password')
        else:
            print(f'Your balance is: {account_balance:.2f}')

    elif action == 'd':
        print('Get Deposit: ')
        user_deposit_amount = int(input('Please enter amount to deposit: '))
        user_password = input('Please enter the password: ')
        if user_password != account_password:
            print('Incorrect password')

        if user_deposit_amount < 0:
            print('You cannot deposit a negative amount!')
        else:
            account_balance += user_deposit_amount
            print(f'Your new balance is: {account_balance}')

    elif action == 's':
        print('Show:')
        print(f'Name {account_name}')
        print(f'Balance: {account_balance}')
        print(f'Password: {account_password}')
        print()

    elif action == 'w':
        print('Withdraw:')
        user_withdraw_amount = int(input('Please enter the amount to withdraw: '))
        user_password = input('Please enter the password: ')
        if user_password != account_password:
            print('Incorrect password for this account')
        elif user_withdraw_amount < 0:
            print('You cannot withdraw a negative amount')
        elif user_withdraw_amount > account_balance:
            print('You cannot withdraw more than you have in your account')
        else:  # OK
            account_balance -= user_withdraw_amount
        print(f'Your new balance is: {account_balance}')

print(f'{"|GOOD BYE|":-^82}')
print('👋🏼')

