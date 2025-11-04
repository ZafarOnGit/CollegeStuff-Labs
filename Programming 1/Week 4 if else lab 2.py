grade = float(input("What's your grade? "));
if (grade < 60):
    print(f"Sorry, but your grade of {grade} is under the passing criteria, please contact your advisor for the next action");
elif (grade <= 80):
    print("Congratulations, you have passed");
else:
    print ("Congratulations, you have passed with distiniction");
