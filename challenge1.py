# Define a function to convert 12-hour time to 24-hour time
def convert_to_24_hour(hour, minute, period):
    # Check if the period is "pm" and hour is not 12
    if period == "pm" and hour != 12:
        hour += 12  # Add 12 hours to convert to 24-hour format
    # Check if the period is "am" and hour is 12
    elif period == "am" and hour == 12:
        hour = 0  # Set hour to 0 to represent midnight in 24-hour format
    
    # Format the time as a four-digit string with leading zeros
    return f"{hour:02d}{minute:02d}"

# Example usage
time_12_hour = "8:30 pm"
hour, minute = map(int, time_12_hour[:-6].split(":"))  # Extract hour and minute from the input string
period = time_12_hour[-2:]  # Extract the period (am/pm) from the input string
time_24_hour = convert_to_24_hour(hour, minute, period)  # Call the conversion function
print(time_24_hour)  # Print the result, e.g., "2030" for "8:30 pm"
