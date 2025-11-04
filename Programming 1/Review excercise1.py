'''
get number of movies to be rented from user
if the number of movies to be rented is less than 5
    then calculate final cost is 50 x number of movies
else 
    calculate final cost with discount as 0.80 x 50 x number of movies

display final cost to user
'''

# here number is the total number of movies rented by user
number = float(input("Enter number of movies: "));
# if the number of movies rented is less than 5, then there will be no discount applies
if number < 5:
    finalcost = 50*number;
# if the number of movies rented is greater than 5, then there will a discount applied
else:
    finalcost = 0.80*50*number;
print(f"final cost is {finalcost}")