# Else: Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#Example: Print all numbers from 0 to 5, and print a message when the loop has ended:
#Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  print(x)
else:
  print("Finally finished!")