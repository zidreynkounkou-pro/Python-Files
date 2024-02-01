
# Get the current time
current_time = datetime.now().time()

# Check if the current time is in the morning (AM)
if current_time.hour < 12:
    print("Current time is in the morning (AM)")
else:
    print("Current time is in the afternoon (PM)")