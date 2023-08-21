# Define a function to check if exactly two out of three integers are positive
def two_are_positive(a, b, c):
    # Check if all three integers are positive
    if a > 0 and b > 0 and c > 0:
        return False  # Return False if all are positive
    
    # Check if exactly two integers are positive
    if a > 0 and b > 0:
        return True  # Return True if a and b are positive
    if a > 0 and c > 0:
        return True  # Return True if a and c are positive
    if b > 0 and c > 0:
        return True  # Return True if b and c are positive
    
    # If none of the above conditions are satisfied, return False
    return False

# Example usage
a = 2
b = -1
c = 3
result = two_are_positive(a, b, c)
print(result)  # Print the result, e.g., True for the given values
