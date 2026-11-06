# INDEX STAR FROM 0 till LEN -1
list = ["Orange", "Apple", "Banana", "Lychee", "Kiwi", "Apple"]
name ="Akku"

print("Print the list items using loops")
for i in list:
    print(i)

print("\n Print the list items using loops- range()")
l = len(list)
for i in range(l):
    print(list[i])

# 2. Slicing the String:
print("Slicing the list ")

print("Specfic item from the list:" , list[2:5])
print("Specfic item from the list:" , list[:5])
print("Specfic item from the list:" , list[5:])
print("Specfic item from the list:" , list[-3:])

# 3. Modifying :
#    1. append - Add item at the end of the list
#    2. Extend - Alll mutiple item in the list - at the end
#    3. Insert - Insert on any index
#    4. remove - remove any item from the list
#    5. clear  - clear the list


list = ["Orange", "Apple", "Banana", "Lychee", "Kiwi", "Apple"]

print("\nAdd the item at the end of the list:")
list.append("BlueBerry")
list.append("Strawberry")
print(list)

print("\n Extend the item at the end of the list:")
list.extend(["Pineapple", "Plum", "JackFruit"])
print(list)

print("\n Insert the item in between the list:")
list.insert(1,"Peach")
print(list)

print("\n Remove the item from the list:")
list.remove("Peach")
print(list)

print("\n Clear the all item from the list:")
list.clear()
print(list)