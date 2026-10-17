def calculate_total(price, quantity):
    total = price * quantity
    return total


def calculate_change(payment, total):
    if payment < total:
        shortage = total - payment
        print("Additional amount needed: PHP", shortage)
    else:
        change = payment - total
        print("Change: PHP", change)


price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))


total = calculate_total(price, quantity)
print("Total Cost: PHP", total)


calculate_change(payment, total)


# DOCUMENTATION QUESTIONS

# 1. The calculate_total() function multiplies the price by the quantity. 
# The calculate_change() function checks if the payment is enough and 
# displays the change or the addidtional amount needed.

# 2. Parameters are the variables in the function definition like the 
# price and quantity. Meanwhile, arguments are the actual values passed to 
# function when it is called, for example is the 35 and 3 in calculate_total(35, 3).

# 3. The returned total is stored in the variable total. It's reused as an
# argument in calculate_change(payment, total).

# 4. It's useful to separate total calculation from change calculation to make
# the code easier to understand, test, or fix because each function has 
# its own specific task.

