#function for arithmetic operation
def add(num_1, num_2):
    return num_1+num_2
def subtract(num_1, num_2):
    return num_1-num_2
def multiply(num_1, num_2):
    return num_1*num_2
def divide(num_1, num_2):
    return num_1/num_2
#try again function
def try_again():
    again = None
#asking for user input and checking it
    while again is None:
        answer = input('\nWould you like to try and use the calculator again? ')
#if yes program runs again
        if answer in ["Y", "YES", "yes", "Yes", "y"]:
            again = True
            continue
#if no prints a message
        elif answer in ["N", "NO", "no", "No", "n"]:
            again = False
            print('Thank you for using the calculator!')
            break
#if answer is invalid asks user again
        else:
            print('Try answering either YES or NO')
#return value of again
    return again
#get user input for operation choice
while True:
    try:
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        operation = input("Please choose from the operations above. Enter 1/2/3/4: ")
#get user input for numbers
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
#if add, add numbers
        if operation == 1:
            answer = add(num_1, num_2)
#if subtract, subtract numbers
        elif operation == 2:
            answer = subtract(num_1, num_2)
#if multiply, multiply numbers
        elif operation == 3:
            answer = multiply(num_1, num_2)
#if divide, divide numbers
        elif operation == 4:
            answer = divide(num_1, num_2)
        else:
            print("Invalid input. Choose an operation by entering a number from 1 to 4.")
#print output
        print("Result =", answer)
#call try again function
        again = try_again()
#exception handling for invalid inputs
    except ZeroDivisionError:
        print("Syntax Error. Cannot be divided by zero. Please try again!")
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A NUMBER")