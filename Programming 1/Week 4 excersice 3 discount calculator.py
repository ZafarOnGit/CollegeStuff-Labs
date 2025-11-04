cost = float(input("Enter your total cost in AED"))
if cost >= 1000:
    print("Eligible for 10 percent discount");
    discount = cost/10;
    cost -= discount;
else:
    print("Not eligible for discount");

print(f"Your total cost is {cost}");