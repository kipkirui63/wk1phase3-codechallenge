Author
KIPKIRUI SANG;
Technology used
Python:
A versatile and widely used high-level programming language known for its simplicity and readability. The solutionS mainly involve functions, conditional statements, arithmetic operations, and string formatting.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

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

You can reach me on :
Email: enocksang8356@@gmail.com
Mattermost: @kipkirui Enock
Linkedin: @enock-sang
License
This project is licensed under the MIT License.

Copyright (c) [2023] [Chepkoech Faith]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.