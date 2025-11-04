price=(input("enter the price"))

if price.isdigit() == True:
    print("price is a number")
    price=float(price)
    vat = price * 0.1
    final = price + vat
    print("Price after VAT is:", final);
else:
    print("Not an integer");