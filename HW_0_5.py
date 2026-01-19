THRESHOLD = 10

def analyze_numbers(a: int, b: int, threshold: int):
    small_numbers = []
    large_numbers = []

    results = {
        "Sum": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else None,
        "Remainder": a % b if b != 0 else None
    }

    for name, value in results.items():
        if isinstance(value, (int, float)):
            judgment = "large" if value >= threshold else "small"
            if judgment == "small":
                small_numbers.append(value)
            else:
                large_numbers.append(value)

            print(f"{name}: {value} is {judgment}")
        else:
            print(f"{name}: N/A")

    return small_numbers, large_numbers

def print_reverse_for(numbers):
    for value in reversed(numbers):
        print(value)

def print_reverse_while(numbers):
    k = len(numbers) - 1
    while k >= 0:
        print(numbers[k])
        k = k - 1

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

small, large = analyze_numbers(a, b, THRESHOLD)

print("\nSmall numbers (for loop):")
print_reverse_for(small)

print("\nLarge numbers (for loop):")
print_reverse_for(large)

print("\nSmall numbers (while loop):")
print_reverse_while(small)




