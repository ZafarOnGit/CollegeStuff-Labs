cost = float(input("Enter your total cost in AED"))
if cost >= 2000:
    print("Eligible for 10 percent discount");
    discount = cost/10;
elif cost >= 1000:
    print("Eligible for 5 percent discount");
    discount = cost/20;
else:
    print("Not eligible for discount");
cost -= discount;
print(f"Your total cost is {cost}");