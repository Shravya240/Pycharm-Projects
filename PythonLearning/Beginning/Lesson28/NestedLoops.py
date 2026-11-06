# Pattern :
'''
 1 2 3 4     - row 1
 1 2 3 4     - row 2
 1 2 3 4     - row 3
'''

for a in range(1,4):    # outer loops   Row 3
    for b in range(1,5):  # Inner loops
        print(b, end ="")    #1 2 3 4
    print()


