import math

def main():

    while True:
        print("What do you want to do:\n1) Test for ValueError\n2) Test for IndexError\n3) Test for ZeroDivisionError\n4) Test for TypeError\n0) Stop")

        try:
            oper = int(input("Your choice:\n"))
        except:
            print("ValueError happened. Enter the selection as an integer.")
            oper = int(input("Your choice:\n"))

        if oper == 1:
            try:
                integer = int(input("Give a non-negative integer:\n"))
                math.sqrt(integer)
            except:
                print("ValueError happened. Non-negative number expected for square root.")
            
        elif oper == 2:
            numbers = [11, 22, 33, 44, 55]
            try:
                index = int(input("Input index 0-4:\n"))
                numbers[index]
            except:
                print("Got an IndexError, index {}.".format(index))
            
        elif oper == 3:
            try:
                divider = input("Enter divider:\n")
                100/divider
            except:
                print("ZeroDivisionError occurred, divider 0.")
            
        elif oper == 4:
            try:
                number = int(input("Enter number:\n"))
            except:
                print("Got TypeError, word*word with strings failed.")

        elif oper == 0:
            break

main()
