from datetime import datetime, time
import csv

print("Inkom Emporium")
print()

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary

def main():
    try:
        product_dict = read_dictionary("products.csv", key_column_index=0)
        with open("request.csv", "rt") as new_file:
            reader = csv.reader(new_file)
            next(reader)
            sum = 0
            sum_one = 0

            for row in reader:
                product, quantity = row  # Unpack the product and quantity from the row
            

                try:
                    product_number = product_dict[product]
                except KeyError:
                    print(f"KeyError: '{product}' key not found in product_dict")
                    continue

                product_name = product_number[1]
                product_price = product_number[2]

                print(f"{product_name}: {quantity} @ {product_price}")
                # Get the current date and time from the computer's system
                current_date_and_time = datetime.now()
                current_time = datetime.now().time() # This is for exceeding requirements
                
                int_number = int(quantity)
                sum += int_number
                # Find the Subtotai.
                product_price = float(product_price)
                sum_one += (product_price * int_number)
                # Compute the sales tax amount.
                if current_time.hour < 11: # This is for exceeding requirements
                    sales_tax = (sum_one * 10) / 100
                else:    
                    sales_tax = (sum_one * 6) / 100
                # Compute the total amount.
                total = sales_tax + sum_one
               

            print()
            print(f"Number of items: {sum}")
            print(f"Subtotal: {sum_one:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {total:.2f}")
            print()
            print("Thank you for shopping at the Inkom Emporium.")
            print(f"{current_date_and_time:%A %B %I:%M %p %Y}")


    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except PermissionError as permission_error:
        print(permission_error)

if __name__ == "__main__":
    main()
