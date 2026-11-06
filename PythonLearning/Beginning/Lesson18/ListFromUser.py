list = []
#ask how many items user wants in list
n= int(input("Enter the number of items you wish to add in the list: "))     #4 items

#repetition 4 times to get usser input
for i in range(n):           #n=4    0,1,2,3   n-1
    item= input("Enter your item: ")
    list.append(item)
print(list)


