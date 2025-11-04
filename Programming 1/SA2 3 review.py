age = float(input("Please enter your age: "))
if age < 13:
    print("You are not eligible to watch a PG-13 movie")
elif age > 60:
    print("You are eligible to watch a PG-13 movie, with a senior discount");
elif age > 13:
    print("You are eligible to watch a PG-13 movie")