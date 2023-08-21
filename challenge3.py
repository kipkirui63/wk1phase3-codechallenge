def two_positive_integers(a, b, c):# This function takes three integer arguments (a, b, c) and checks if exactly two of them are positive.

    positive_count = 0  # Initialize the count of positive numbers below

    if a > 0:
        positive_count += 1  # Increment count if a is positive
    if b > 0:
        positive_count += 1  # Increment count if b is positive
    if c > 0:
        positive_count += 1  # Increment count if c is positive

    return positive_count == 2  # The function returns True if exactly two numbers above are positive, and False if otherwise.

#input the numbers and store them in their respective variables
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Calls two_positive_integers function with the provided inputs and stores the result in the result variable.
result = two_positive_integers(a, b, c)

print(f"({a}, {b}, {c}) == {result}")# Print the result in the format "(a, b, c) == result"