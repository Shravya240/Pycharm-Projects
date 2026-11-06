# Formula : ax + b = cx + d

def linearAlgebraSolution(a,b,c,d):
    return (d-b)/(c-a)


a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))
d = float(input("Enter d :"))

x = (d-b)/(a-c)

print("Algebra: ", x)

