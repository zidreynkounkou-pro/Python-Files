Child_Price_Meal = float(input("What is the price of a children's meal?: "))
Adult_Price_Meal = float(input("What is the price of an adult's meal?: "))
Number_Of_Children = int(input("How many children are there?: "))
Number_Of_Adult = int(input("How many adults are there?: "))
Sales_Tax_Rate = float(input("What is the sales tax rate?: "))

print(" ")

# Subtotal calculation
Total_Children_Price_Meal = Child_Price_Meal*Number_Of_Children
Total_Adults_Price_Meal = Adult_Price_Meal*Number_Of_Adult
The_Meal_Subtotal = Total_Children_Price_Meal + Total_Adults_Price_Meal
print(f"Subtotal: ${The_Meal_Subtotal:.2f}")

# Sales Tax rate calculation
Sales_Tax = The_Meal_Subtotal*Sales_Tax_Rate/100
print(f"Sales Tax: ${Sales_Tax:.2f}")

# Price total Meals calculation incuding Sales Tax Rate
Amount_To_Pay = The_Meal_Subtotal + Sales_Tax
print(f"Total: ${Amount_To_Pay:.2f}")

print(" ")

# Payment amount and change
Payment_Amount = float(input("What is the payment amount?: "))
Change_Amount = Payment_Amount - Amount_To_Pay
print(f"Change: ${Change_Amount:.2f}")