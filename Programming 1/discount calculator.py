
def calculate_discount(cost):
    discount_amount = cost*0.05
    print("Your calculated discount for cost of", cost, "is", discount_amount)
    return discount_amount;


cost = float(input("enter your cost"))
discount = calculate_discount(cost)

print("Your calculated discount for cost of", cost, "is", discount)