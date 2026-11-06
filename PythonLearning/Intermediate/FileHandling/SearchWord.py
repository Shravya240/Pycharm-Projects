
def check_word(search_word):

    with open("names.txt") as file:
        content = file.read()

        if content.find(search_word) == -1:
            print("Not Found")
        else:
            print("Found")

check_word("Aarnavi")


print("Reading the files through for loops: ")
with open ("names.txt") as file:
    for line in file:
        print(line.strip())