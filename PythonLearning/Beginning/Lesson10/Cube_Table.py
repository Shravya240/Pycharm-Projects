num = int(input("Enter your last number: "))
result = ""
for i in range(1, num + 1):
    result += str(i * i * i) + " "
print(result)
