def calculate_final_cost(cost, vat):
    final_cost = cost + (cost*vat/100)
    return final_cost;

x = float(input("What is the cost of the item:"))
y = float(input("Enter the vat rate (in percentage):"))

output = calculate_final_cost(x,y)
print(output)