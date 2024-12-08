user = {
    'pin': '9999'
    'balance' '500'
    }

print("Welcome to the Toby ATM")
pin = int("Insert your pin now (For testing purposes, your pin is 9999)")
if pin == user['Pin']:
    print("Enter 1 if you wish withdraw cash. 2 if you wish to see balance. 3 if you wish to deposit cash or 4 if you wish to see your recent transactions")
else:
    print("Wrong Pin, Please retry")
if condition:
    input == 1:
    withdrawal()
elif:
    input ==2:
    balance()
elif:
    input == 3:
    deposit()
elif:
    input == 4:
    transactions()
else:
print("That is not an option. Enter 1 if you wish withdraw Cash or 2 if you wish to see balance.")


def withdrawal():
    amount = int(input("Enter the amount you'd like to take out")
                 if amount > user['balance']
                 print("Insufficient funds")
                else:
                    user['Balance'] = user['balance'] - amount
                    print [{amount}" successfully taken out"]

def balance():
print user['balance']

def deposit():
    amount = int(input("Enter the amount you'd like to deposit")
                 user['Balance'] = user['balance'] + amount
                 print [{amount}" successfully taken out"]

def transactions():
print("06/12/2024 - Deposit - Toby ATM: £35")
print("05/12/2024 - Withdrawal - Toby ATM: £30")
print("03/12/2024 - Pepe's Chicken: £45")
print("01/12/2024 - Amazon: £50")
print("30/11/2024 - Test Purchase: £5")
