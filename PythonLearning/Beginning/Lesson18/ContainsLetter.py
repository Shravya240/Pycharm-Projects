list = ['English', 'French', 'Hindi', 'German', 'Russian', 'Spanish', 'Chinese', 'Korean']
count = 0
for item in list:
    if item == "Apple":
        count = count + 1
print("Sum:", count)

print("\n Solution 2: Exist or not ")
list = ["Apple", "Banana" ,"Peach", "Fruits", "Blueberry", "Apple"]
for item in list:
    if item == "Apple":
       print('It exists')
       break
    else:
        print("It doesn't exist")

print("\n Solution 3: Exist or not with in operator")
list = ["Apple", "Banana" ,"Peach", "Fruits", "Blueberry", "Apple"]
for item in list:
    if "Apple" in list:
       print('It exists')