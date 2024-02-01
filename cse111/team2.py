from datetime import datetime
# prompt for the subtotal
subtotal = float(input("Please enter the subtitle: "))
# determine the current date and time from the operating system
current_date_and_time = datetime.now()
# determine the day of the week from the current date and time
day_of_the_week = current_date_and_time.weekday()
# taxes
tax = 0.06
# calculate the sales tax amount
sales_tax_amount = subtotal * tax
# calculate the subtotal, taxes included
subtotal_with_tax = subtotal + sales_tax_amount
# check if the it's tuesday or wednesday and the subtotal is greater or equal to 50
# then apply the 10% discount
if day_of_the_week in (1,2) and subtotal >= 50:
    discount = subtotal * (10/100)
    new_subtotal = subtotal - discount
    new_sales_tax_amount = new_subtotal * tax
    new_total = new_subtotal + new_sales_tax_amount
    # print the results
    print(f"Sales tax amount: {round(new_sales_tax_amount, 2)}")
    print(f"Total: {round(new_total, 2)}")
else: # when the day of the week is not  tuesday or wednesday
    total = subtotal_with_tax
    print(f"Sales tax amount: {round(sales_tax_amount, 2)}")
    print(f"Total: {round(total, 2)}")
print(f"{current_date_and_time: %y-%m-%d}")