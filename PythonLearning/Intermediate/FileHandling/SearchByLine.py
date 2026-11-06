with open("names.txt") as namefile:  # 1. Open the File
    var_content = namefile.read()    # 2. Read the File - Read() - read entire file  : Read the file
    word = "Shravya"                # 3. Search the Word  - Which Operator i should use ?
    print(word in var_content)      # Check for the word if it exists or not

#OR

with open("names.txt") as namefile:  # 1. Open the File
    for eachline in namefile:
        if eachline.strip() == "Shravya":
            print("found")


with open("names.txt") as namefile:  # 1. Open the File
    var_content = namefile.read()    # 2. Read the File - Read() - read entire file  : Read the file   as String
    word = "Shravya"                 # 3. Search the Word  - using the String Function
    if var_content.find(word.strip()) :
        print("Found")
    else :
        print("Not Found")