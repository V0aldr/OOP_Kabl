"""
Основная программа, контролирующая банк, состоящий из счетов
"""

from bank import Bank
# создаем экземпляр банка
o_bank = Bank()

# Основной код
# создаем два тестовых счета
joesAccountNumber = o_bank.createAccount('Joe', 100, 'JoesPassword')
print("Joe's account number is:", joesAccountNumber)
marysAccountNumber = o_bank.createAccount('Mary', 12345, 'MarysPassword')
print("Mary's account number is:", marysAccountNumber)


if __name__ == '__main__':

    while True:
        print()
        print('To get an account balance, press b')
        print('To close an account, press c')
        print('To make a deposit, press d')
        print('To open a new account, press o')
        print('To quit, press q')
        print('To show all accounts, press s')
        print('To make a withdrawal, press w ')
        print()
        action = input('What do you want to do? ')
        action = action.lower()
        action = action[0]  # берем первую букву
        print()
        if action == 'b':
            o_bank.balance()
        elif action == 'c':
            o_bank.closeAccount()
        elif action == 'd':
            o_bank.deposit()
        elif action == 'o':
            o_bank.openAccount()
        elif action == 's':
            o_bank.show()
        elif action == 'q':
            break
        elif action == 'w':
            o_bank.withdraw()
        else:
            print('Sorry, that was not a valid action. Please try again.')

    print('Done')
