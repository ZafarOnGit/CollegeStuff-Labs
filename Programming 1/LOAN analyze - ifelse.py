Annual_income = float(input("Please enter your annual income: "));
Employment_years = float(input("How many years have you been employed at your current job?: "));
if Annual_income >= 20000 and Employment_years >= 3:
    print("Elible for loan");
else:
    print("Sorry, but you are not eligible for loan")