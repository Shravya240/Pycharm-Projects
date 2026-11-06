quiz = {
    "Argentina" : "Buenos Aires" ,
    "Australia" : "Canberra" ,
    "Canada" : "Ottawa" ,
    "China" : "Beijing" ,
    "France" : "Paris" ,
    "Germany" : "Berlin" ,
    "India" : "New Delhi" ,
    "Italy" : "Rome",
    "Japan": "Tokyo",
    "Mexico": "Mexico City" ,
    "Russia": "Moscow",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Brazil": "Brasilia",
    "United States": "Washington D.C"
        }

def main():

    for question in quiz:
        print("What is the Capital for", question, "?")
        ans = input().lower()
        print(ans)
    if (ans == quiz[question].lower()):

        print("Correct !!!, Capital of ", question, "is ", quiz[question])
    else:
        print("Sorry Wrong, Capital of ", question, "is ", quiz[question])

print()

main()
