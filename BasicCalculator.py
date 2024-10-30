def add(a,b):
    result = a+b
    return result

def subtract(a,b):
    result = a-b
    return result

def multiply(a,b):
    result = a*b
    return result

def divide(a,b):
    result = a/b
    return result


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operation = int(input("1 = add, 2 = subtract, 3 = multiply, 4 = divide: "))


if operation == 1:
    equals = add(num1,num2)
elif operation == 2:
    equals = subtract(num1,num2)
elif operation == 3:
    equals = multiply(num1,num2)
elif operation == 4:
    equals = divide(num1,num2)
else:
    equals = "Not valid operation"

print("Result: " + str(equals))
