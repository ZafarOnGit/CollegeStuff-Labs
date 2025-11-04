sum = 0 
count = 0 

for number in range(5,16):
    if number != 10:
        sum+=number

    if number % 2 !=0:
        count += 1

print(sum)
print(count)
