import random
import string
import secrets

def generate_password(length):
    password = ""
    character = string.ascii_letters + string.digits + string.punctuation
    for n in range(length):
        password = password + secrets.choice(character)
        #or
        #password = password + random.choice(character)
    return password


passw = generate_password(8)
print(passw)