import art
import os

operations = ['+', '-', '*', '/']


def calculate(n1, n2, o):
    if operations.index(o) == 0:
        return n1 + n2
    elif operations.index(o) == 1:
        return n1 - n2
    elif operations.index(o) == 2:
        return n1 * n2
    else:
        return round(n1/n2, 2)


while True:
    print(art.logo)
    num1 = float(input("What is the first number? "))
    op = input("What is the operation [+ - * /]?")
    num2 = float(input("What's the next number? "))

    res = calculate(num1, num2, op)
    print(f"{num1} {op} {num2} = {res}")

    while True:
        choice = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")
        if choice == "n":
            os.system('cls')
            break
        else:
            op = input("Pick an operation [+ - * /]?")
            num = float(input("What's the next number? "))
            res2 = calculate(res, num, op)
            print(f"{res} {op} {num} = {res2}")
            res = res2
