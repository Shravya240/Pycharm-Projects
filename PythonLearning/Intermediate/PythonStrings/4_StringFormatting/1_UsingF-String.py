''' Use f-strings to print:
------------------------------------
F-string allows you to format selected parts of a string.
1. To specify a string as an f-string, simply put an f in front of the string literal, like this:
2. To format values in an f-string, add placeholders {}, a placeholder can contain
    a. Variables,
    b. Operations,
    c. functions,
    d. modifiers to format the value.
    [ A modifier is included by adding a colon : followed by a legal formatting type,
     like .2f w
which means fixed point number with 2 decimals]

'''
# 1. Create an f-string:

txt = f"The price is 49 dollars"
print(txt)
# 2. Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59.12548562
txt = f"The price is {price:.3f} dollars"
print(txt)

name = "Sandy"
print("Hello ", name)

print(f"Hello, {name}")


name = "Sandy"
age = 15

print(f"Hello, My name is {name} and I am {age} year old")
print("Hello, My name is", name, "and I am " ,age , "year old")
