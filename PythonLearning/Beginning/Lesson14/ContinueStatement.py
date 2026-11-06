#Problem 2: Countinue Example
#iterate numbers from a list using a for loop and calculate its square. If we found a number greater than 10, we will
#not calculate its square and directly jump to the next number.
#Use the if condition with the continue statement. If the condition evaluates to true, then the loop will move to the
#next iteration


num = (10,20, 30, 40, 50, 87, 100, 104, 129, 154)

for i in num:
    if i>100:
        continue
    print(i)