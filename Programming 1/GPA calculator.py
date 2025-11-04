total = 0.0
x = int(input("Enter the total number of courses: "))
for i in range(1,x+1,1):
    GPA  = float(input("Enter the GPA in course " + str(i) +": " ))
    total += GPA;
print("The average GPA is:", total/i)