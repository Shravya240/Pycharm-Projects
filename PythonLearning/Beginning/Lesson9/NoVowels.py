str= "Welcome"
vowels= "a, e, i, o, u"
result= ""

for i in str:
    if i not in vowels:
        result += i

print(result)