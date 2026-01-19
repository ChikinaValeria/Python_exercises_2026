THRESHOLD = 10

list_of_small_numbers=[]
list_of_large_numbers=[]

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


def add_to_list(judgment: str, value, list_of_small_numbers, list_of_large_numbers):
    if judgment == "small":
        list_of_small_numbers.append(value)
    else:
        list_of_large_numbers.append(value)


# loop with ternar operator
for name, value in results.items():
    if isinstance(value, (int, float)):
        judgment = "large" if value >= THRESHOLD else "small"
        add_to_list(judgment, value, list_of_small_numbers, list_of_large_numbers)
        print(f"{name}: {value} is {judgment}")
    else:
        print(f"{name}: {value}")

print(f"List of small nambers: {list_of_small_numbers}")
print(f"List of large numbers: {list_of_large_numbers}")

# the new list is created, not good for big data
for i in list_of_small_numbers[::-1]:
    print(i)

for j in reversed(list_of_large_numbers):
    print(j)