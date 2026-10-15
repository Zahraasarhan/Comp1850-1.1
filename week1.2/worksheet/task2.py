# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if not numbers:
    sys.exit("Error: no numbers provided")
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

numbers.sort()
middle = len(numbers) // 2

if len(numbers) % 2 == 0:
    median = (numbers[middle - 1] + numbers[middle]) / 2
else:
    median = numbers[middle]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")