print("Welcome to the shopping cart program!\n")

items = []
prices = []
action = -1
different_options = ["Add item","View cart","Remove item","Compute total","Items quantity","Quit"]

while action != 6:
    
    try: # Exceed requirements.
        # Display the menu system
        print("Please select one of the following: ")
        for option in enumerate(different_options):
            print(f"{option[0] + 1}. {option[1]}")

        action = int(input("Please enter an action: "))

        # Add the item and price to the shopping cart list.
        if action == 1:
            item = input("What item would you like to add? ").title()
            price = float(input(f"What is the price of '{item}'? "))
            items.append(item)
            prices.append(price)
            print(f"'{item}' has been added to the cart.\n")
            continue  

        # Show the contents of the shopping cart.
        elif action == 2:
            print("The contents of the shopping cart are: ")
            for i in range(len(items)):
                shopping_cart = items[i]
                price = prices[i]   
                print(f"{i + 1}. {shopping_cart} - ${price:.2f}")
            print()
        # Remove an item from the shopping cart.
        elif action == 3:
            remove_item = int(input("Which item would you like to remove? "))
            # Check if the index entered is not in the shopping cart list.
            if remove_item - 1 not in range(len(items)):
                print("Sorry, that is not a valid item number.\n")
            else:
                items.pop(remove_item -1)
                # Remove the price of the item from the shopping cart list.
                prices.remove(prices[remove_item -1])
                print("Item removed. \n")
            continue

        # Compute the total price of the items in the shopping cart.
        elif action == 4:
            total = 0
            for nth_price in prices:
                total += nth_price
            if items == []: # Exceed requirements
                print("Sorry, there are no items in the shopping cart.\n")
            else:
                print(f"The total price of the items in the shopping cart is: ${total:.2f}\n")
                
            # Check the quantity of the items in the shopping cart. 
        elif action == 5:
            quantity = len(items)
            #check if the quantity of the items in the shopping cart is equal to 0 or 1.
            if quantity == 0 or quantity == 1:
                print(f"There are {quantity} item in the shopping cart.\n")
            else:
                # Check the quantity of the items in the shopping cart is equal to more than one item.
                if quantity > 1:
                    print(f"There are {quantity} items in the shopping cart.\n")
        # End.
        if action == 6:
            print("Thank you. Goodbye.")

    except: # Exceed requirements.
        print("ERROR: Enter one of the indexes from the manue, please.\n")  
