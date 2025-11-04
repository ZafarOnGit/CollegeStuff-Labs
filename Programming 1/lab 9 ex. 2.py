print("WELCOME TO CALCULATOR APP")
while True:
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
        elif (operator == "sub"):
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
        choice = input("Do you have another calculation (y/n) ");
        choice = choice.lower()
        if(choice=="n"):
            break;