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
