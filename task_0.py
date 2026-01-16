"""

Implement a function that asks the user for consumption in consumed units and the unit
price (these should be handled as floating-point numbers) and calculates and displays
the total price based on the given information.
The total price is calculated by multiplying the consumption by the unit price,
adding a 17% tax, and then adding a margin of 4.32 currency units if the consumption is less than 500 units,
and 7.75 currency units otherwise.

"""

def calculation():
    cons = float(input('Consumption?'))
    price = float(input('Unit price?'))



    if cons < 500:
        margin = 4.32
    else:
        margin = 7.75


    total = cons*price*1.17 + margin

    print(f"Total price is {total} currency units.")
    print(f"Calculations: {cons} * {price} * 1.17 + margin {margin}")

calculation()
