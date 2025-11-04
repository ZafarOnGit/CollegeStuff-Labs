'''
Get input rolecode from user
If rolecode is 
'''
print("~~Role Codes~~");
print("Faculty - FA");
print("Academic programme chair - APC");
print("Division chair - DC");
role = input("Please enter your role based on role codes");
if (role == "FA"):
    print("You have been assigned Faculty chair");
elif (role == "APC"):
    print("You have been assigned Academic Program Chair");
elif (role == "DC"):
    print("You have been assigned Division Chair");
else:
    print("Unknown role")