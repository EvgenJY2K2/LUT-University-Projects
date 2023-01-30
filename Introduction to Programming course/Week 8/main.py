import L08T2Library

def menu():
    print("What temperature conversion do you want to do?\n1) Celsius->Fahrenheit\n2) Celsius->Kelvin\n3) Fahrenheit->Kelvin\n4) Fahrenheit->Celsius\n5) Kelvin->Celsius\n6) Kelvin->Fahrenheit\n0) Stop")
    action = int(input("Your choice:\n"))
    return action

def main():
    print("Using version 1.0 of the temperature conversion library.")

    while True:
        oper = menu()

        if oper == 1:
            temp = int(input("Enter the starting temperature:\n"))
            t = L08T2Library.cel_fah(temp)
            print("Temperature in degrees Fahrenheit:", round(t, 2))
            print("")
        elif oper == 2:
            temp = int(input("Enter the starting temperature:\n"))
            t = L08T2Library.cel_kel(temp)
            print("Temperature in degrees Kelvin:", round(t, 2))
            print("")
        elif oper == 3:
            temp = int(input("Enter the starting temperature:\n"))
            t = L08T2Library.fah_kel(temp)
            print("Temperature in degrees Kelvin:", round(t, 2))
            print("")
        elif oper == 4:
            temp = int(input("Enter the starting temperature:\n"))
            t = L08T2Library.fah_cel(temp)
            print("Temperature in degrees Celsius:", round(t, 2))
            print("")
        elif oper == 5:
            temp = int(input("Enter the starting temperature:\n"))
            t = L08T2Library.kel_cel(temp)
            print("Temperature in degrees Celsius:", round(t, 2))
            print("")
        elif oper == 6:
            temp = int(input("Enter the starting temperature:\n"))
            t = L08T2Library.kel_fah(temp)
            print("Temperature in degrees Fahrenheit:", round(t, 2))
            print("")
        else:
            break
main()
