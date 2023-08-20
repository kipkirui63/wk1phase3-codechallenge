# wk1phase3-codechallenge
This repository contains Python code examples that demonstrate various concepts and tasks. Each example is explained and accompanied by code snippets that you can use and modify for your own projects.
##
1. Converting 12-Hour Time to 24-Hour Time
File: convert_12_to_24_hour.py

This code snippet demonstrates how to convert a 12-hour time format (e.g., "8:30 pm") to a 24-hour time format (e.g., "2030").

Usage:

python
Copy code
time_12_hour = "8:30 pm"
hour, minute = map(int, time_12_hour[:-6].split(":"))
period = time_12_hour[-2:]
time_24_hour = convert_to_24_hour(hour, minute, period)
print(time_24_hour)  # Output: "2030"

###
2. Calculating Average Heat Level of Spicy Foods
File: average_heat_level.py

This code demonstrates how to calculate the average heat level of a list of spicy foods based on their heat levels.

Usage:

python
Copy code
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    # ... other spicy foods ...
]

avg_heat = average_heat_level(spicy_foods)
print(f"Average Heat Level: {avg_heat:.2f}")

###
3. Finding Highest Value of Consonant Substrings
File: highest_consonant_value.py

This code snippet shows how to find the highest value of consonant substrings in a lowercase string of alphabetic characters.

Usage:

python
Copy code
input_string = "abcdefghijklmnopqrstuvwxyz"
result = highest_consonant_value(input_string)
print(result)  # Output: 71