#Check If Number is divisible by both 5 and 7 or not

num= int(input("Enter your number: "))
if (num%5== 0 and num%7 == 0):
    print("Your number is divisable by both 5 and 7")
elif (num % 5 == 0):
    print("Your number is divisable by only 5")
elif (num%7== 0):
    print("Your number is divisable by only 7")
else:
    print("Your number is not divisible by either number")