try:# I used this oparator to try showing creativity

    # writing a function to calculate and return the wind chill based on a given temperature and wind speed.
    def wind_chill(t,v):
        cal_wind_chill = 35.74 + (0.6215) * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16) 
        return cal_wind_chill

    # writing a function to convert from Celsius to Fahrenheit
    def celsius_into_fahrenheit(t,v):
        t = t * (9 / 5) + 32
        cal_wind_chill = 35.74 + (0.6215) * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
        return cal_wind_chill

    # prompting the user for the temperature  
    t = float(input("What is the temperature? "))
    c_or_f = input("Celsius or Fahrenheit (C/F)? ")

    # this variable is only applicable when the temperature is given in celsius
    # it allows me to print the temperature in fahrenheit for each wind speed
    f = t * (9 / 5) + 32

    # checking either the temperature is given in celsius or fahrenheit and, then, looping through
    # wind speeds from 5 to 60 miles per hour, incrementing by 5,
    # and calculate and display the wind chill for each of these wind speeds.
    if c_or_f.lower() == "f":
        for v in range(5,61,5):
            cal_wind_chill = wind_chill(t,v)
            print(f"At temperature {t: .1f}F, and wind speed {v} mph, the windchill is: {cal_wind_chill: .2f}F")
    else:
        for v in range(5,61,5):
            cal_wind_chill = celsius_into_fahrenheit(t,v)
            print(f"At temperature {f: .1f}F, and wind speed {v} mph, the windchill is: {cal_wind_chill: .2f}F")
except:
    print("ERROR: run the code again then, enter a value either in celsius or fahrenheit.")
