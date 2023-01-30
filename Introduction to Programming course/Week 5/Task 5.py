def menu():
    print("Select one of the following operations:\n1) Enter integers\n2) Sum\n3) Division\n0) Stop")
    operation = int(input("Select the function (0-3):\n"))
    return operation

def enter_integer(text):
    value = int(input(text))
    return value

def sum(value1, value2):
    sum = value1 + value2
    return "Sum " + str(value1) + " + " + str(value2) + " = " + str(sum)

def division(value1, value2):
    if value2 == 0:
        return ("You cannot divide by zero.")
    else:
        div = round((value1/value2), 2)
        return "Division " + str(value1) + " / " + str(value2) + " = " + str(div)

def main():
    while True:
        action = menu()

        if action < 0 or action > 3:
            print("Unknown choice, try again.")
            continue

        if action == 1:
            x = enter_integer("Enter first integer: \n")
            y = enter_integer("Enter second integer: \n")
            print("You inputted integers %s and %s"%(x, y))
            continue

        elif action == 2:
            print(sum(x, y))

        elif action == 3:
            print(division(x, y))
            
        else:
            print("Bye.")
            break
main()
