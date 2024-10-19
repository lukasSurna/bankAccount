
accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password
    
def show():
    global accountName, accountBalance, accountPassword
    print('     Name', accountName)
    print('     Balance:', accountBalance)
    print('     Password:', accountPassword)
    print()
    
def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount')
        return None
    
    if password != accountPassword:
        print('Incorrect password')
        return None
    
    accountBalance += amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if password != accountPassword:
        print('Incorrect password')
        return None
    
    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    
    accountBalance -= amountToWithdraw
    return accountBalance

newAcc = ('Lukas', 20, 'hi')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make deposit')
    print('Press w to make withdrawal')
    print('Press s to show account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    print()
    
    if action == 'b':
        print('Get balance: ')
        userPassword = input('Please enter your password:')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')
            
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password: ')
        
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print(f'Your new balance is: {newBalance}')
            