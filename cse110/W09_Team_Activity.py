numbers = []
number = ""
while number != 0:
    try:
        number = int(input("Type a list of numbers, type 0 when finished: "))
        if number != 0:
            numbers.append(number)

    except:
        print("ERROR: please enter a number.")
        
    
smallest_positive_num = min([n for n in numbers if n > 0])
sorted_list =  sorted(numbers)

print(f"The sum is: {sum(numbers)}")
print(f"The average is: {sum(numbers)/len(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The smallest positive number is: {smallest_positive_num} \n")
print("The sorted list is:")

for i in sorted_list:
    print(i)






