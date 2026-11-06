print("Temperature Converter")
temp= int(input("Enter the temperature: "))
unit= str(input("Enter the unit (C or F): "))
if unit == "C":
    print(temp * 1.8 + 32, "F")
else:
    print((temp - 32) / 1.8, "C")

