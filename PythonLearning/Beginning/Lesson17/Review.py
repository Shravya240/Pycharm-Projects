# Data Types

# String: Text Value
# Numeric: Int, Float, Complex
# Boolean: boolean
# List: Group of data- unordered, unchangeable, duplicates []
            #["aarav", "akku", "dfd"]
            #[45,823,5462,27]
            #["fenna", 67, "True"]
#set no duplicate () /tuple/dictionary: group of data-

list = ["Orange", "Apple", "Banana", "Lychee", "Kiwi", "Apple"]
# INDEX STAR FROM 0 till LEN -1
name ="Akku Shravya"
#output: •A-K-K•U

print("1. Print the Name in the String")
for i in name:
    print (i)

print("2. Print the Name in the String")
len =len (name)
for i in range(len):
    print (name [i])

 # 2. Slicing the String:  [start: stop] [ < index: 0›:stop] [start: ‹len >]

print("3. Slicing the String using [:]")
middle= name[5:12]
print(middle)

print("3. Slicing the String using [:]")
first= name [:4]
print(first)

print("3. Slicing the String using [:]")
last= name [13:15]
print(last)

#Negative Indexing Slicing

print("4. Negative Indexing Slicing the String using [:]")
last= name[-2:1]
print(last)

name ="Akku Shravya kk"
print("5. Negative Indexing Slicing the String using [:]")
m= name[-6:-3]
print(m)

# 3. upper, lower, strip
print("1. Using Functions print all letters in uppercase: upper ()")
name = "Akku"
name = name.upper ()
print (name)

print("2. Using Functions print all letters in lowercase: lower ()")
name = "Akku"
name = name. lower ()
print (name)

print("3. Using Functions remove all whitespace in the words: strip()")
name = "    Akku    "
name = name.strip()
print (name )

print("4. Using Functions replace a letter from another letter: k, r")
name = "Akku KK Kiran"
name = name.replace("k" ,"r")
print (name )

