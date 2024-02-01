# max and min variables
max_value = -1
min_value = 100000000000000
# open the file
with open("life-expectancy.csv") as file:
    # Delete the header so, an error will not occur when converting the data into a float.
    next(file)
    for line in file:
        # delete whitespaces
        clean_line = line.strip()
        # split the data the data into different parts
        parts = clean_line.split(",")
        # life expectancy part
        life = parts[3]

    # Find the max and min values:
        # max value
        if float(life) > max_value:
            max_value = float(life)
            # min value
        elif float(life) < min_value:
            min_value = float(life)
    # print the max and min values
    print(f"The overall max life expectancy is {max_value}")
    print(f"The overall min life expectancy is {min_value}")