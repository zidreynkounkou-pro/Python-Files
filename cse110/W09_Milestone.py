print("Welcome to the shopping cart program!\n")

items = []
action = -1
different_options = ["Add item","View cart","Remove item","Compute total","Quit"]
item_position = 0


while action != 5:
    print("Please select one of the following: ")
 
    for option in enumerate(different_options):
        print(f"{option[0] + 1}. {option[1]}")

    action = int(input("Please enter an action: "))
    if action == 1:
        item = input("What item would you like to add? ")
        items.append(item)
            
        print(f"'{item}' has been added to the cart.\n")
        continue  

    elif action == 2:
        print("The contents of the shopping cart are: ")
        for shopping_cart in items:
            print(shopping_cart)
        print()
        continue
    
    if action == 5:
        print("Thank you. Goodbye.")

        





