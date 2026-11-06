#for i in range(1,11):
    #print(i)

#for i in str("Welcome"):
    #print(i)

str = "Welcome"
#print(str[::-1])

#str = "Welcome"
      #0123456
#for i in str:
   # print(i)


#print(str[1:3]) #el
#print(str[2:]) # lcome
#print(str[:]) # Welcome
#print(str[::-1]) # emocleW



#Program1 : Count the No. of VOwels

str = 'Welcome'
count = 0

for letter in str:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count = count + 1
print(count)


str = "Welcome"
count =0
for letter in str:
    if letter in ['a','e','i','o','u']:
        count = count + 1
print(count)


str = "Welcome"
count =0
for letter in str:
    if letter in 'aeiou':
        count = count + 1
print(count)

