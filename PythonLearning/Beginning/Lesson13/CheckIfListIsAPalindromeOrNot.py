list = [100,200,300,200,100]
reverselist = list[:: -1]

#if list == reverselist:
if list == list[::-1]:
    print("List is Palindrome")
else:
    print("List is Not a Palindrome")