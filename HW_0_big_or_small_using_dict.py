THRESHOLD = 10

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# creating dict
results = {
    "Sum": a + b,
    "Subtraction": a - b,
    "Multiplication": a * b,
    "Division": a / b if b != 0 else "N/A",
    "Remainder": a % b if b != 0 else "N/A"
}

print(f"\nAnalysis (Threshold: {THRESHOLD})")

# loop with ternar operator
for name, value in results.items():
    if isinstance(value, (int, float)):
        judgment = "large" if value > THRESHOLD else "small"
        print(f"{name}: {value} is {judgment}")
    else:
        print(f"{name}: {value}")