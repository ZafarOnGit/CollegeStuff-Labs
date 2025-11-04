#Simple calculator HW1 week 5

'''
This program is a simple calculator
first it asks the user to enter a number
then it asks for the second number
Then it asks the user to select the operation (Addition, multiplication division)
then in calculates the number and prints the output
'''

print("WELCOME TO CALCULATOR APP")
Number1 = float(input("Please enter your first digit    "))
Number2 = float(input("Please enter your second digit   "))
print("For addition type add")
print("For subtraction type sub")
print("For multiplication type mul")
print("For division type div")
operator = input("Please enter your input   ")

if (operator == "add"):
    Number1 += Number2
    print(Number1);
elif (operator == "add"):
    Number1 -= Number2
    print(Number1);
elif (operator == "mul"):
    Number1 *= Number2
    print(Number1);
elif (operator == "div"):
    Number1 /= Number2
    print(Number1);
else:
    print("Error, invalid operation")