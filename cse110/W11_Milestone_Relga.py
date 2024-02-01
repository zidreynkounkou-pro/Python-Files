import csv
# an empty list for the life expectancy data
life_expectancy = []
# max and min variables
max_value = -1
min_value = 100000000000000
# open the file
with open("life-expectancy.csv") as file:
    
    # creating DictReader object
    new_file = csv.DictReader(file)

    # Adding the third part of the dataset into the empty list
    # I am using this method so, I can put each part of the dataset into a list and iterate through them when needed
    for f in new_file:
    

        life_expectancy.append(f["Life expectancy (years)"])

    # findind both the max and min life expectancies
    for i in range(len(life_expectancy)):

        # max life expectancy
        if float(life_expectancy[i]) > max_value:
            max_value = float(life_expectancy[i])

        # min life expectancy
        elif float(life_expectancy[i]) < min_value:
            min_value = float(life_expectancy[i])
        

    # printing the max and min life expectancies
    print(f"The overall max life expectancy is {max_value}")
    print(f"The overall min life expectancy is {min_value}")

        
    
                
        
    