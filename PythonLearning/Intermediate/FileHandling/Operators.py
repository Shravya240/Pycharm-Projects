"""
List of Operator :
--------------------------
1. Arithmetic Operator   [  +  -  *   /   %(Mod) //(Floor Diviion) ]  = Calculation
2. Comparison Operator   [ >    <   >=    <=  ==  !=   ]              = Checking if right(True) or wrong(False)  (One Condition)
3. Logical Operator ( AND, OR, NOT)                                   = (More than One Condition)
4. Membership Operator (in)                                           = Checking if you exists(True) or not(False)
5. Identity Operator                                                  = same indentity- same value and type (True) or not (False)



"""
# 1. Arithmetic Operator
print(5+6)     # 11
print(9-7)     # 2

# 2. Comparison Operator
print(9>5)     # True
print(9>23)    # False

# 3. Logical Operator ( AND, OR, NOT)
print("A: ", 9>25 and 9>3)      # False and True    =   False
print("B: " , 9>25 or 9>3)       # False or True     =   True
print("C:", 9>25 and (9>3 or 9>17))     # (False   and (True  or   False) )   = (False  and  True)  =  False

print("D: ", not(9>25))         # not(False)  = True
print("E:", not(9>25 and (9>3 or 9>17))   )

# 4. Membership Operator  (in)

var_str = "Python is great language to learn to interact with computer and write any algorithms"

print("Java" in var_str)     # True
# 5. Identity Operator  - # same value and type (True)  or not  (False)

var_a = 34
var_b = 34

print(var_a is var_b)         # True


var_a = 34
var_b = 43
print(var_a is var_b)       # False


var_a = 34
var_b = "34"

print(var_a is var_b)       # False