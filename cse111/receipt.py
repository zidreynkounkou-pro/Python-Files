from datetime import datetime, time
import csv
# Print the store name
print("Inkom Emporium")
print()
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
        """
    # Let's open the products.csv file.
    dictionary = {} # This is the compound dictionary.
    with open(filename, "rt") as file:
        # Read the file.
        reader = csv.reader(file)
        #Let's skip the first row of the file as it only contains the column headings.
        next(reader)
        # Iterate through the file.
        for row in reader:
                
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary
def main():
    try:
        # Calling the read_dictionary function.
        product_dict = read_dictionary("products.csv", key_column_index = 0)
        # Let's open the request.csv.
        with open("request.csv", "rt") as new_file:
            # Read the file the new_file.
            reader = csv.reader(new_file)
            # Let's skip the first row of the new_filw that contains the headings.
            next(reader)
            
             # Get the current date and time from the computer's system
            current_date_and_time = datetime.now()
            current_time = datetime.now().time()

            # The somme variables
            sum = 0
            sum_one = 0
        
            # Let's iterate through the reader file.
            for file_name in reader:
                # Let's unpack product and quantity from the file_name
                product, quantity = file_name
                try:# Check if the product ordered is in the product_dict
                    product_number = product_dict[product]
                # Handle the KeyError       
                except KeyError as key_error:
                    print(type(key_error).__name__, key_error, end = "")
                    print(" Sorry, cannot found this item in the store!")
                    
                    continue
                product_name = product_number[1]
                product_price = product_number[2]
            
                # Print the list of ordered items.
                print(f"{product_name}: {quantity} @ {product_price}")
                # Number of ordered items.
                int_number = int(quantity)
                sum += int_number
                # Find the Subtotal.
                product_price = float(product_price)
                sum_one += (product_price * int_number)
                # Compute the sales tax amount.
                if current_time.hour < 11: # Exceeding the requirements
                    sales_tax = (sum_one * 10)  / 100
                else:
                    sales_tax = (sum_one * 6)  / 100
                # Compute the total amount.
                total = sales_tax + sum_one
                        
            # Print the number of ordered items.
            print()
            print(f"Number of items: {sum}")
            # Print the Subtotal.
            print(f"Subtotal: {sum_one: .2f}")
            # Print the sales tax amount.
            print(f"Sales Tax: {sales_tax: .2f}")
            # Print the Total amount due.
            print(f"Total: {total: .2f}")
            # The thank you message.
            print()
            print("Thank you for shopping at the Inkom Emporium.")
            # Print the current date and time.
            print(f"{current_date_and_time: %A %B %I:%M:%S %p %Y}")
                    
    # Handle exceptions
    
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except PermissionError as permission_error:
        print(permission_error)
        
# Call the main function
if __name__ == "__main__":
    main()
            
     
                
                    
                    
        