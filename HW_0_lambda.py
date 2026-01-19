
THRESHOLD = 10
a, b = 8, -7

# Анонимная функция: принимает x, возвращает строку
judge = lambda x: "large" if x > THRESHOLD else "small"

results = {
    "Sum": a + b,
    "Sub": a - b,
    "Mul": a * b,
    "Div": a / b,
    "Rem": a % b
}

for name, val in results.items():
    print(f"{name}: {val} is {judge(val)}")
