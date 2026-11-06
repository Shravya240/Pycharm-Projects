def add():
    pass
def subtract():
    pass

def multiplication():
    pass

def division(a, b):
    try:
        a = int(a)
        b = int(b)
        result = a/b
    except ZeroDivisionError:
        print("Can't Divide by Zero")
    except:
        print("Please check your Value")
    else:
        print("Division:" , result)


if __name__ == "__main__":    # Entry Point of Program
    num1 = input("Enter the Number 1: ")
    num2 = input("Enter the Number 2: ")
    division( num1 , num2)