Username= str(input("Enter your Username: "))

if Username == "Shravya":
    Password = str(input("Enter your Password: "))
    if Password == "pythonisgreat":
        print("Login Succesful")
        print("Hello, Shravya")
    else:
        print("Password incorrect")
        print("Login failed.")
else:
    print("Incorrect username")
    print("Login failed.")