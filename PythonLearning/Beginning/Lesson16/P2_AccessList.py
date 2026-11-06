# 2. Access the lists:
thelist= ["banana", "pineapple", "watermelon", "apple", "banana", "cherry"]
#index : 0
print(thelist[0])
print(thelist [1])


# Slicing the list of items from list - Specific list of data using : opereator

print(thelist[0:2]) # Start - included and stop - not included
print(thelist[:4]) # start = 0, end = 3
print(thelist[2:]) # start = 2 , end = length of the list

#Negative Indexing
print(thelist[-1]) # last item of the list
print(thelist[-2]) # second last items from the list

print(thelist[-4:])