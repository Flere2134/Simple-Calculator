import time
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
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        while True:
            operation = (input("Please choose from the operations above. Enter 1/2/3/4: "))
            if operation in ["1", "2", "3", "4"]:
                break
            else:
                print("Invalid input. Please try again.")
#get user input for numbers
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
        answer = 0
#if add, add numbers
        if operation == "1":
            answer = add(num_1, num_2)
#if subtract, subtract numbers
        elif operation == "2":
            answer = subtract(num_1, num_2)
#if multiply, multiply numbers
        elif operation == "3":
            answer = multiply(num_1, num_2)
#if divide, divide numbers
        elif operation == "4":
            answer = divide(num_1, num_2)
        else:
            print("Invalid input. Choose an operation by entering a number from 1 to 4.")
            continue
#print output
        time.sleep(1)
        print("Result =", answer)
#try again
        while True:
            again = input("Do you want to use the calculator again? (yes/no): ")
            if again in ["Y", "YES", "yes", "Yes", "y", "N", "NO", "no", "No", "n"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if again in ["N", "NO", "no", "No", "n"]:
            print("Thank you for using the calculator!")
            break
#exception handling for invalid inputs
    except ZeroDivisionError:
        print("Syntax Error. Cannot be divided by zero. Please try again!")
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A NUMBER")