# Loops: repetition
    # start, end , increment

# 1. For Loops
# 2. While Loops

for i in range(0,11,1):
    print(i)

a=0    #start a=0
while (a<11):    # keep going till the conidition is valid
    print(a)
    a += 1  #a = a + 1

a=0
name ="Akku"  #4
while(a<len(name)):
    print(name[a])
    a = a + 1

list = ["Jai", "Verru", "Sharukh", "Salman"]
start=0
end = len(list)
while(start<end):
    print(list[start])
    start = start +1