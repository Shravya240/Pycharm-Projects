# Creating a dictionary
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# printing the dictionary
print(country_capitals)

#Output:
#{'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'}

# Access the Dictionary Item
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London


#Add Items to a Dictionary
#We can add an item to a dictionary by assigning a value to a new key.

country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
}

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

print(country_capitals)


#Remove Dictionary Items
#We can use the del statement to remove an element from a dictionary.

country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
}

# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)
#Output:
#{'Canada': 'Ottawa'}


#Change Dictionary Items
#Python dictionaries are mutable (changeable). We can change the value of a dictionary element by referring to its key.

country_capitals = {
  "Germany": "Berlin",
  "Italy": "Naples",
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)

#Output:
#{'Germany': 'Berlin', 'Italy': 'Rome', 'England': 'London'}

#Iterate Through a Dictionary: Loops (For)
#A dictionary is an ordered collection of items (starting from Python 3.7), therefore it maintains the order of its items.
#We can iterate through dictionary keys one by one using a for loop.

country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome"
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)
print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


#Find Dictionary Length
#We can find the length of a dictionary by using the len() function.

country_capitals = {"England": "London", "Italy": "Rome"}

# get dictionary's length
print(len(country_capitals))   # Output: 2

numbers = {10: "ten", 20: "twenty", 30: "thirty"}

# get dictionary's length
print(len(numbers))            # Output: 3

countries = {}

# get dictionary's length
print(len(countries))          # Output: 0


#Dictionary Membership Test  (in Operators)

#We can check whether a key exists in a dictionary by using the in and not in operators.

file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True

# Note: The in operator checks whether a key exists; it doesn't check whether