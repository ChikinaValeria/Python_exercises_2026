THRESHOLD = 10

def calculate_results(a: int, b: int) -> dict:
    return {
        "Sum": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else None,
        "Remainder": a % b if b != 0 else None
    }

def print_analysis(results: dict, threshold: int) -> None:
    print(f"\nAnalysis (Threshold: {threshold})")
    for name, value in results.items():
        if isinstance(value, (int, float)):
            label = "large" if value >= threshold else "small"
            print(f"{name}: {value} is {label}")
        else:
            print(f"{name}: N/A")

def classify_results(results: dict, threshold: int):
    small_numbers = []
    large_numbers = []

    for value in results.values():
        if isinstance(value, (int, float)):
            if value >= threshold:
                large_numbers.append(value)
            else:
                small_numbers.append(value)
    return small_numbers, large_numbers

def print_reverse_for(numbers: list) -> None:
    for value in reversed(numbers):
        print(value)

def print_reverse_while(numbers: list) -> None:
    k = len(numbers) - 1
    while k >= 0:
        print(numbers[k])
        k -= 1

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

results = calculate_results(a, b)
print_analysis(results, THRESHOLD)

small_numbers, large_numbers = classify_results(results, THRESHOLD)

print("\nSmall numbers (for loop):")
print_reverse_for(small_numbers)

print("\nLarge numbers (for loop):")
print_reverse_for(large_numbers)

print("\nSmall numbers (while loop):")
print_reverse_while(small_numbers)
