"""

Create a program that asks the user to enter two numbers.
Print the results of addition, subtraction, multiplication, and division of the numbers,
as well as the remainder of their division, to stdout using the print command.

"""

a, b = int(input("Enter the first number: ")), int(input("Enter the second number: "))

print(f"The sum of {a} and {b} is {a+b}.")
print(f"The substraction result of {a} and {b} is {a-b}.")
print(f"The multiplication result of {a} and {b} is {a*b}.")
print(f"The devision result of {a} and {b} is {a/b}.")
print(f"The reminder of the devision of {a} and {b} is {a%b}.")

# Add a feature that classifies (using if–else branches) the result values calculated in Point 1 into small and
# large numbers (based on some threshold value of your choice) and prints its judgment (small/large) for each value.

def is_small_number (num: int) -> bool:
    if num < 5:
        return True
    else:
        return False


