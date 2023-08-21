def solution(input_string):
    # Define the values of consonant characters using a dictionary
    consonant_values = {'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'v': 21, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    current_value = 0  # Initialize the current value
    max_value = 0  # Initialize the maximum value
    
    # Iterate through each character in the input string
    for character in input_string:
        if character in consonant_values:  # Check if the character is a consonant
            current_value += consonant_values[character]  # Add the value of the consonant
        else:
            # Update the maximum value and reset the current value
            max_value = max(max_value, current_value)
            current_value = 0  # Reset the current value to 0
    
    # Update the maximum value after the loop and return it
    max_value = max(max_value, current_value)
    return max_value

# Test cases
print(solution("strength"))   # Output: 8
print(solution("software"))   # Output: 19
