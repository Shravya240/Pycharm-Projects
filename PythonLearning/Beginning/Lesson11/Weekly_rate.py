hours = int(input("Enter your working hours: "))
rate = int(input("Enter your hourly rate: "))
weekly = (hours * rate * 7)

if (weekly <= 1,000):
    print("You cannot afford to live alone")
else:
    print("You can afford to live alone")