def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1/n2

calc = {"+": add, "-": sub, "*": multiply, "/": divide,}
import artcalc
def calculator():
    print(artcalc.logo)
    if_continue = True
    n1 = float(input("What's the first number? "))

    while if_continue:
        for op in calc:
            print(op)
        operator = input("Enter operator: ")

        if operator not in calc:
            print("Invalid operator. Try again.")
            continue

        n2 = float(input("What's the next number? "))
        ans = calc[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {ans}")
        choice = input(f"Type 'y' to continue calculating with {ans} and 'n' to exit.\n")

        if choice == 'y':
            if isinstance(ans, str):
                print("Cannot continue calculation due to error.")
                break
            n1 = ans
        else:
            if_continue = False
            print("Thank you for visiting!")
calculator()