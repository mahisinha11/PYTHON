# Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Display the results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# Take user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate to form full name
full_name = first_name + " " + last_name

# Print personalized greeting
print("Hello, " + full_name + "! Welcome!")
