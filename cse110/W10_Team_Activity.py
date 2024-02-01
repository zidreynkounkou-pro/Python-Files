names = []
balances = []
name = None

'''Enter the names and balances of bank accounts (type: quit when done)
What is the name of this account? checking
What is the balance? 238.12
What is the name of this account? savings
What is the balance? 392.99
What is the name of this account? quit

Account Information:
0. checking - $238.12
1. savings - $392.99

Total: $631.11
Average: $315.56
Highest balance: savings - $392.99

Do you want to update an account? yes
What account index do you want to update? 0
What is the new amount? 200

Account Information:
0. checking - $200.00
1. savings - $392.99

Do you want to update an account? yes
What account index do you want to update? 1
What is the new amount? 425.50

Account Information:
0. checking - $200.00
1. savings - $425.50

Do you want to update an account? no

Account Information:
0. checking - $200.00
1. savings - $425.50
Sample Solution'''
print('Enter the names and balances of bank accounts (type: quit when done)\n')

while name != "quit":
    
    name = input('What is the name of this account? ')

    if name != "quit":
        balance = int(input('What is the balance? '))
    
        names.append(name)
        balances.append(balance)
        
    
    if name == "quit":
        print()
        print('Account Information:')

        for i in range(len(names)):
            name = names[i]
            balance = balances[i]
        
            print(f"{i}. {name} - ${balance}")
        break
total = 0
for balance in balances:

    total += balance
print(f"\nTotal: ${total}")

average = total / len(balances)
highest_balance = 0


print(f"Average: ${average:.2f}")

for i, balance in enumerate(balances):
    if balance > highest_balance:
        highest_balance = balance
        highest_balance_name = names[i]

print(f"Highest balance: {highest_balance_name} - ${highest_balance}\n")

update_account = "yes"
while update_account.lower() == "yes":
    update_account = input("\nDo you want to update an account? ")
    if update_account.lower() == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = int(input("What is the new amount? "))
        balances[index] = new_amount

        print(f"\nAccount Information:")

        for i in range(len(balances)):
            new_balance = balances[i]
            name = names[i]
            print(f"{i}. {name} - ${new_balance}")

    #if update_account.lower() == "no":
print(f"\nAccount Information:")

for i in range(len(balances)):
    balance = balances[i]
    name = names[i]
    print(f"{i}. {name} - ${new_balance}")
        
    





