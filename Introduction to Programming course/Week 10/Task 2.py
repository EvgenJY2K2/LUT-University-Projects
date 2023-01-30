import csv, sys

def menu():
    print("-1) Stop\n0) Calculate Airplanes\n1) Calculate Helicopters\n2) Calculate Ultralights\n3) Calculate Gliders and Powered Gliders\n4) Calculate Autogiros\n5) Calculate Balloons (hot-air)\n6) Calculate Airships")
    action = input("Please, make your selection:\n")
    return action

def main():
    name = input("Enter filename: ")

    try:
        file = open(name, "r", encoding="utf-8")
    except:
        print("Error processing file '{}', stopping.".format(name))
        sys.exit(0)

    content = file.readlines()
    data = []
    info = []
    
    for row in content[1:]:
        data.append(row.strip('\n'))
    print(data[28])

    print("The file contains {} aircrafts".format(len(data)))

    for aircraft in data:
        info.append(aircraft.split(";"))
    print(info[28])

    while True:
        oper = menu()

        try:
            oper = int(oper)
        except:
            print("Faulty selection. Please try again.")
            sys.exit(0)

        if oper == 0:
            ages = []
            missing = 0
            proper = 0
            
            for item in info:
                name = ''.join(item[3:5])
                print(name)
                try:
                    age = float(item[6])
                    ages.append(age)
                    proper = proper + 1
                except:
                    surname = item[3]
                    surname = surname.rstrip('\"')

                    name = item[4]
                    name = name.lstrip('\"')

                    print("{},{} was missing age".format(surname, name))
                    missing = missing + 1

            print("We had {} passengers with missing age".format(missing))
            print("We have {} passengers with proper age\n".format(proper))

        elif oper == 1:
            
            print("We had {} passengers with missing cabin".format())
            print("We have {} passengers with proper cabin".format())

        elif oper == 2:
            
            print("We had {} passengers with missing age".format())
            print("We have {} passengers with proper age".format())
            print("Average age of all {} passengers was {} years".format())
        elif oper == 3:
        elif oper == 4:
        elif oper == 5:
        elif oper == 6:

        elif oper == -1:
            break

        else:
            break

main()
