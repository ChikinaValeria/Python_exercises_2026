"""

Create a list containing 50 (pseudo)random float values between 4.0 and 7.0.
Determine the arithmetic mean, median, and the smallest value from the list.

"""

import random

numbers = []

for i in range(50):
    num = random.uniform(4.0, 7.0)
    numbers.append(num)

mean_value = sum(numbers)/len(numbers)

min_value = min(numbers)

sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n%2 == 1:
    median_value = sorted_numbers[n//2]
else:
    median_value = sorted_numbers[n//2-1] + sorted_numbers[n//2] / 2

print("Numbers: ", numbers)
print("Mean: ", mean_value)
print("Minimun: ", min_value)
print("Median: ", median_value)
