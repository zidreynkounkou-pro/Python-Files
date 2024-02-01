# empty lists 
list_life = []
list_country = []

# total
total = 0

choice_max_value = -1
choice_min_value = 8888888888988

print("*********************************************************************************")
user = input("* Enter the year of interest:")
print("*")
# max and min variables
max_value = -1
min_value = 100000000000000
# open the file
with open("life-expectancy.csv") as file:
    # Delete the header so, an error will not occur when converting the data into a float.
    next(file)
    # iterate through the file line by line
    for line in file:
        # delete whitespaces
        clean_line = line.strip()
        # split the data into different parts
        parts = clean_line.split(",")
        # life expectancy part
        life = parts[3]
        # years
        year = parts[2]
        # conuntries
        country = parts[0]

        # Find the max and min values:
        # max value
        if float(life) > max_value:
            max_value = float(life)
            max_year = year
            max_country = country
        
        # min value
        elif float(life) < min_value:
            min_value = float(life)
            min_country = country
            min_year = year

        # treat the user's request
        if user == year:
            list_life.append(life)
            list_country.append(country)

    for i, choice_life_exp in enumerate(list_life):
        # find the total, then average according to the user's choice
        total += float(choice_life_exp)
        average = total / len(list_life)

        # find the max value and country according to the user's choice
        if float(choice_life_exp) > choice_max_value:
            choice_max_value = float(choice_life_exp)
            choice_max_country = list_country[i]

        # find the min value and country according to the user's choice
        elif float(choice_life_exp) < choice_min_value:
            choice_min_value = float(choice_life_exp)
            choice_min_country = list_country[i]

# print the max and min values (countries included)
print("*********************************************************************************")
print(f"* The overall max life expectancy is: {max_value} from {max_country} in {max_year:19} *")
print(f"* The overall min life expectancy is: {min_value} from {min_country} in {min_year:19} *")
print("*                                                                               *")
# print the user's request
print("*********************************************************************************")
print("* For the year " + user + ":")
print(f"* The average life expectancy across all countries was {average: .2f}")
print(f"* The max life expectancy was in {choice_max_country} with {choice_max_value}")
print(f"* The min life expectancy was in {choice_min_country} with {choice_min_value}")
print("*********************************************************************************")