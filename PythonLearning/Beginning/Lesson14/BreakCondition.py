#Problem1 : Break Example
#iterate numbers from a list using a for loop, and if we found a number greater than 100, we will break the loop.
#Use the if condition to terminate the loop. If the condition evaluates to true, then the loop will terminate. Else loop
#will continue to work until the main loop condition is true

num = (10,20, 30, 40, 50, 87, 104, 129, 154)

for i in num:
    if i>100:
        break


    print(i)
