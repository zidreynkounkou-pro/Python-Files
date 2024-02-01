print(" ")
child_price_meal = float(input("What is the price of a children's meal? "))
adult_price_meal = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adult = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
print(" ")

# Subtotal calculation
total_children_price_meal = child_price_meal * number_of_children
total_adults_price_meal = adult_price_meal * number_of_adult
the_meal_subtotal = total_children_price_meal + total_adults_price_meal
print(f"Subtotal: ${the_meal_subtotal:.2f}")

# Sales Tax rate calculation
sales_tax = the_meal_subtotal * sales_tax_rate / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Price total Meals calculation incuding Sales Tax Rate
amount_to_pay = the_meal_subtotal + sales_tax
print(f"Total: ${amount_to_pay:.2f}")

print(" ")

# Payment amount and change
payment_amount = float(input("What is the payment amount?: "))
change_amount = payment_amount - amount_to_pay
print(f"Change: ${change_amount:.2f}")

# My adds

if payment_amount < amount_to_pay:
    print("")
    print(f"Please, your payment amount (${payment_amount}) is less than the amount you are charged to pay (${amount_to_pay}). You need to add ${amount_to_pay - payment_amount:.2f} or more. Thank you for your understanding!")
else:
    print(" ")
    print("We appreciate your participation, thank your dear friend!")
print(" ")

