#Projects: Contact Name List

namelst = ["Aravi", "Suhani", "Alinaa", "Akku"]

def viewContacts():
    print("List of Name in the Address Book")
    for name in namelst:
        print(name)

def addContacts(name):
    namelst.append(name)

def deleteContacts(name):
    return   # ToDo - Homework

def verifyUser(name):
    if name in namelst:
        entry ="yes"
    else:
        entry = "no"
    return entry


print("Welcome to Address Book")
aksk= str(input("Login as User or Admin:"))
