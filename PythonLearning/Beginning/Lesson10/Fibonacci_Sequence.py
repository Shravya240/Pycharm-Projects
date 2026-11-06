'''Solution:'''
n = 10
num1 = 0
num2 = 1
# repeat constant start =0, end = 9 (n-1), step = 1 (by default)
for i in range(10): # Loop: start, end (destination)# excluded, steps/ increment +1(by default)

#1. print next in series
    print(num1, end=" ")

#2. add last two numbers to get the next numbers
    res = num1 + num2

#3. update the values
    num1 = num2
    num2 = res


