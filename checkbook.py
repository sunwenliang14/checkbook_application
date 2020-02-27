def current_balance():
    with open("account_balance.txt") as f:
        balances = f.readlines()
        balance = balances[-1]
    return balance

def add_balance(current_balance):
    with open("account_balance.txt","a") as f:
        f.write("\n")
        f.write(str(current_balance))

    
print('~~~ Welcome to your terminal checkbook! ~~~')

def menu():
    print('''What would you like to do?
    
    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit''')  




while True:
    menu()
    user_choice = input("Please choose a number between 1 and 4 ")
    user_choice_int = int(user_choice)
    balance = int(current_balance())
    
    if (user_choice.isdigit() == False or  user_choice_int< 1 or user_choice_int > 4):
        print(f"{user_choice_int} is nice, but it is not a valid number")        
        continue
    elif user_choice_int == 1:
        print(f'Your current balance is {balance}')
    elif user_choice_int == 2:
        transaction = input("How much is the debit?")
        balance -= int(transaction)
        add_balance(balance)
    elif user_choice_int == 3:
        transaction = input("How much is the credit?")
        balance += int(transaction)
        add_balance(balance)
    else:
        print('Thanks, have a great day!')
        break
