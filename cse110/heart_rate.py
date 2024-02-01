"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# prompt the user to enter the age
age = int(input("Please enter your age: "))
# find the minimum and maximum rates
max_value = 220 - age
min_rate = max_value * (65 / 100)
max_rate = max_value * (85 / 100)

# print the results
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min_rate: .0f} and {max_rate: .0f} beats per minute.")
