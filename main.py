import random
balance = 1000

print("Welcome to the Loser's Bank.")

def withdraw(amount, balance):
    if balance > amount and balance > 0:
        balance -= amount
        print(f'Your balance is {balance}')

    else:
        print("That's too much. Unfortunately, you're broke.")

    again = input('Would you like to perform another action? ')
    if again.lower() in ('yes', 'y'):
        play(balance)
    else:
        print('Goodbye!')

    return balance


def deposit(amount, balance):
    if amount > 0:
        balance += amount
        print(f'Your balance is {balance}')
    else:
        print('L')

    again = input('Would you like to perform another action? ')
    if again.lower() in ('yes', 'y'):
        play(balance)
    else:
        print('Goodbye!')

    return balance


def check(balance):
    print(f'Your balance is {balance}')
    again = input('Would you like to perform another action? ')
    if again.lower() in ('yes', 'y'):
        play(balance)
    else:
        print('Goodbye!')


def rob(amount, balance):
    outcomeList = ['1', '2', '3']
    outcome = random.choice(outcomeList)
    if outcome in ('1', '2'):
        balance += amount
        print(f'Your balance is {balance}')
        again = input('Would you like to perform another action? ')
        if again.lower() in ('yes', 'y'):
            play(balance)
        else:
            print('Goodbye!')
    else:
        balance = 0
        print('Uh oh! The police caught you! You lost all of your money, and cannot continue anymore.')
    
    return balance


def leave():
    print('Goodbye!')
    exit()


def play(balance):

    action = input('What would you like to do today? Withdraw, deposit, check, exit, or rob? ')

    if action.lower() == 'withdraw':
        withdrawal = float(input('How much would you like to withdraw?' ))
        balance = withdraw(withdrawal, balance)

    elif action.lower() == 'deposit':
        deposition = float(input('How much would you like to deposit?' ))
        balance = deposit(deposition, balance)

    elif action.lower() == 'check':
        check(balance)
    
    elif action.lower() == 'exit':
        leave()

    elif action.lower() == 'rob':
        robAmount = float(input('Be careful! How much money do you want to rob?' ))
        balance = rob(robAmount, balance)
    
    else:
        print('That is not an action!')
        print('Try again.')
        play(balance)


play(balance)
