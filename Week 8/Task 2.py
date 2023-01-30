import math, random

def menu():
    print("What temperature conversion do you want to do?\n1) Celsius->Fahrenheit\n2) Celsius->Kelvin\n3) Fahrenheit->Kelvin\n4) Fahrenheit->Celsius\n5) Kelvin->Celsius\n6) Kelvin->Fahrenheit\n0) Stop")
    action = int(input("Your choice:\n"))
    return action

def cel_fah(t):
    return
def cel_kel(t):
    return
def fah_kel(t):
    return
def fah_cel(t):
    return
def kel_cel(t):
    return
def kel_fah(t):
    return

def main():
    print("Using version 1.0 of the temperature conversion library.")

    while True:
        oper = menu()
        temp = int(input("Enter the starting temperature:\n"))

        if oper == 1:
            cel_fah(temp)
            print("Temperature in degrees Fahrenheit: ", )
        elif oper == 2:
            cel_kel(temp)
            print("Temperature in degrees Kelvin: ", )
        elif oper == 3:
            fah_kel(temp)
            print("Temperature in degrees Kelvin: ", )
        elif oper == 4:
            fah_cel(temp)
            print("Temperature in degrees Celsius: ", )
        elif oper == 5:
            kel_cel(temp)
            print("Temperature in degrees Celsius: ", )
        elif oper == 6:
            kel_fah(temp)
            print("Temperature in degrees Fahrenheit: ", )
        else:
            break
main()
