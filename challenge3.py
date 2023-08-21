def solution(input_string): #defining a function
    consonant_values = {'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'v': 21, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    current_value = 0
    max_value = 0
    

# "Creating a way to find the biggest value in parts of the word"
    for character in input_string:
        if character in consonant_values:
            current_value += consonant_values[character]
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
            max_value = max(max_value, current_value)

            return max_value

# Test cases
print(solution("hello"))   # Output: 8
print(solution("software"))  # Output: 19
