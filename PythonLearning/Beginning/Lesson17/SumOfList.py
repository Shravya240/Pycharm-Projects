#sum of all the items in list
first= [10,20,30,40] #sum is 100
sum= 0

for i in first:
    sum= sum+i
    print("Loop :" , i , ":" , sum)

print("Total :" , sum)

#Program 1: Sum of the all item in the List:
lst  =[10,20,30,40]   # Sum = 100
sum = 0
for i in lst:
   print("Loops: " , sum , "+ " , i , "=")
   sum = sum + i
   print(sum)
print("Total :" , sum)

'''
10   = 0 +  10 = 10               # Note: Get the value from prev sum 
20   = 10 + 20 = 30
30   = 30 + 30 = 60
40   = 60 + 40 = 100
---
100
'''