total = 0.0
x = int(input("Enter the total number of subjects"))
for i in range(1,x+1,1):
    score  = float(input("Enter your score for subject" + str(i) +": " ))
    total += score;
    average = total/i
print("The total score is: ", total)
if average >= 70.0:
    print("Well done, your average is", average);
else:
    print("Work harder, your average is ", average)