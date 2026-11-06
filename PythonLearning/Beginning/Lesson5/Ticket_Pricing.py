print("Ticket Pricings")
age= float(input("Enter your age: "))
Time= float(input("Enter the current time(in 24 hour format): "))

if (age < 12 and Time < 17):
    print("Your ticket costs $5")
elif (age < 12 and Time >= 17):
    print("Your ticket costs $7")
elif (age >= 12 and age < 60 and Time < 17):
    print("Your ticket costs $10")
elif (age >= 12 and age < 60 and Time >= 17):
    print("Your ticket costs $12")
elif (age >= 60 and Time < 17):
    print("Your ticket costs $7")
elif (age >= 60 and Time >= 17):
    print("Your ticket costs $9")
