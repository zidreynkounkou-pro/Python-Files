print("Welcome to the shopping cart program!\n")

items = []
prices = []
action = -1
different_options = ["Add item","View cart","Remove item","Compute total","Quit"]

while action != 5:
    # Exceed requirements
    try:

        print("Please select one of the following: ")
        for option in enumerate(different_options):
            print(f"{option[0] + 1}. {option[1]}")

        action = int(input("Please enter an action: "))

        # Add the item and price to the shopping cart list
        if action == 1:
            item = input("What item would you like to add? ")
            price = int(input("What is the price of the item? "))
            items.append(item)
            prices.append(price)
            
            print(f"'{item}' has been added to the cart.\n")
            continue  

        # Show the contents of the shopping cart
        elif action == 2:
            print("The contents of the shopping cart are: ")
            for i in range(len(items)):
                shopping_cart = items[i]
                price = prices[i]   
                print(f"{i + 1}. {shopping_cart} - ${price}")
            print()
    
        elif action == 3:
            remove_item = int(input("Which item would you like to remove? "))


            # Check if the index entered is not in the shopping cart list
            if remove_item not in range(len(items)):
                print("Sorry, that is not a valid item mumber.\n")
            else:
                items.pop(remove_item -1)
                # Remove the price of the item from the shopping cart list
                prices.remove(prices[remove_item -1])

                print("Item removed. \n")
            continue
        # Compute the total price of the items in the shopping cart
        elif action == 4:
            total = 0
            for nth_price in prices:
                total += nth_price
            print(f"The total price of the items in the shopping cart is: ${total:.2f}\n")
        # End
        if action == 5:
            print("Thank you. Goodbye.")
    # Exceed requirements
    except:
        print("ERROR: Enter one of the indexes from the manue, please.\n")  

        





