TASK 1


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


number = 5
result = factorial(number)

print("Factorial of", number, "is:", result)


TASK 2

import math


num = float(input("Enter a number: "))


square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)


print("Square root of", num, "is:", square_root)
print("Natural logarithm of", num, "is:", natural_log)
print("Sine of", num, "is:", sine_value)

