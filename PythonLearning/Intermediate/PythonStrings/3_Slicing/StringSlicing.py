text = "687-875-6573"

# First 3 Character of Text:
print(text[ :3]) # start =0 end = 3 # excluded step = 1 [0-2]

# First 7 Character of Text:
print(text[:7])
#start =0 end = 7 # excluded step = 1 [0-6]

# Last 4 Character of Text:
print(text[8:]) # start = 8 end = Len(text) # excluded step = 1
# Fwd Indexing

#Last 4 Character of Text:
print(text[-4:]) # start = 8 end = len(text) # excluded step = 1 # Back Indexing

# SubString: Middle of Text : 875
print(text[4:7]) # start = end = len (text) # excluded step = 1


email = "name@gmail.com"

domain = email[-3:]
if domain == "com":
    print("$65")
elif domain == "org":
    print("$60")
else:
    print("Unknown domain")


