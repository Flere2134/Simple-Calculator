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
#get user input of 1st number 1st then operation then 2nd number
        num_1 = float(input())
        operation = input(())
        num_2 = float(input())
        answer = 0
#if add, add numbers
        if operation == "+":
            answer = add(num_1, num_2)
#if subtract, subtract numbers
        elif operation == "-":
            answer = subtract(num_1, num_2)
#if multiply, multiply numbers
        elif operation == "*":
            answer = multiply(num_1, num_2)
#if divide, divide numbers
        elif operation == "/":
            answer = divide(num_1, num_2)
        else:
            print("Invalid input. Choose an operation by entering a valid symbol (+, -, *, /).")
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