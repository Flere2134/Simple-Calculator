#function for arithmetic operation
def add(num_1, num_2):
    return num_1+num_2
def subtract(num_1, num_2):
    return num_1-num_2
def multiply(num_1, num_2):
    return num_1*num_2
def divide(num_1, num_2):
    return num_1/num_2
#get user input for operation choice
while True:
    try:
        operation = input("Please choose from the operations below. Enter 1/2/3/4: ")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
#get user input for numbers
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
#if add, add numbers
        if operation == 1:
            answer = add(num_1, num_2)
#if subtract, subtract numbers
        if operation == 2:
            answer = subtract(num_1, num_2)
#if multiply, multiply numbers
        if operation == 3:
            answer = multiply(num_1, num_2)
#if divide, divide numbers
        if operation == 4:
            answer = divide(num_1, num_2)
#print output
#ask user input if want to try again
#exception handling for invalid inputs