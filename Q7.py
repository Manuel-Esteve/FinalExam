# Q7:

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

processed_numbers = [] # Create object for desired numbers and function which will carry it out
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        processed_numbers.append(num * 2)  # Replace with double value


print(processed_numbers)