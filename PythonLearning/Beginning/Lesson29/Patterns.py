
'''


*          - row 1
* *        - row 2
* * *      - row 3
* * * *    - row 4

'''


for r in range (1,6):
    for c in range (1, r+1) :
        print("* " * c)


print("Square Matrix")
n = 5
for rows in range(1,n+1):
    for cols in range(1, 6):
        print("*", end= " ")

    print()


print("Triangle Matrix")
for rows in range (1, 5):
    for cols in range(1, rows+1):
        print ("*", end = " ")

    print()




# Hollow Square :
#  *  *  *  *  *
#  *           *
#  *           *
#  *           *
#  *  *  *  *  *

