'''
get price per unit item from user
get No. of items from user
calculate the total cost without vat
calculate the final price with vat
display final cost
'''

price = float(input("enter the price of unit item: "));
number = float(input("enter the total units of item: "));
TotalPrice = price*number;
Vat = TotalPrice*0.05

TotalPrice += Vat
#alternatively, you can simply do FinalPrice = TotalPrice + Vat and print FinalPrice
print (f"The total price is: AED {TotalPrice}");