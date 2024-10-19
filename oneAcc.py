accountName = 'Lukas'
accountBalance = 1000
accountPassword = 'hello'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make deposit')
    print('Press w to make withdrawal')
    print('Press s to show account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0] #just use first letter
    
    if action == 'b':
        print('Get balance: ')
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print(f'Your balance is: {accountBalance}')
    
    elif action == 'd':
        print('Deposit: ')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password: ')
        
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')
            
        elif userPassword != accountPassword:
            print('Incorrect password')
        
        else:
            accountBalance += userDepositAmount
            print(f'Your new balance is: {accountBalance}')
            
    elif action == 's':
        print('Show: ')
        print(f'    Name: {accountName}')
        print(f'    Balance: {accountBalance}')
        print(f'    Password: {accountPassword}')
        print()
    
    elif action == 'q':
        break
    
    elif action == 'w':
        print('Withdraw: ')
        
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        
        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')
            
        elif userPassword != accountPassword:
            print('Incorrect password for this account')
            
        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')
        
        else:
            accountBalance -= userWithdrawAmount
            print(f'Your new balance is: {accountBalance}')
        
    print('Done')