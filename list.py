fruits = ["apple", "bannana", "cherry"];
print(fruits)
print(fruits[2])


print("the list is", fruits)

fruits.append("Orange")
print(fruits)

fruits.insert(1, "Mango");

fruits.pop();
print(fruits)

fruits.pop(2);
print(fruits)

fruitpopped=fruits.pop(2);
print(fruits);
print(fruitpopped);

fruits.remove("Mango")
print(fruits)