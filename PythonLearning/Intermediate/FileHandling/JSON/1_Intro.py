import json
str = '{"name" : "Mohit", "age" : 30}'
dict = {"name" : "Mohit", "age": "30"}

print (str)
print(dict)

file = json.loads(str)

print(file["name"])
print(file["age"])

import json
dict = {"name": "Mohit", "age": 30}
file1 = json.dumps(dict)
print(file1)