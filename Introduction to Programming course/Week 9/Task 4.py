import csv, sys

def menu():
    print("You can do the following\n1) Calculate passengers with missing ages\n2) Calculate passengers without a cabin\n3) Calculate average age of passengers (skip missing ages)\n0) Stop")
    action = input("Your choice:\n")
    return action

def main():
    print("Welcome to Titanic passenger analyzer")
    name = input("Enter filename for titanic data:\n")

    try:
        file = open(name, "r")
    except:
        print("Error processing file '{}', stopping.".format(name))
        sys.exit(0)

    content = file.readlines()
    data = []
    info = []
    
    for row in content[1:]:
        data.append(row.strip('\n'))
    print(data[147])

    print("The file contains {} passengers\n".format(len(data)))

    for passenger in data:
        info.append(passenger.split("\,"))
    print(info[28])

    while True:
        oper = menu()

        try:
            oper = int(oper)
        except:
            print("Faulty user input. Exiting.")
            sys.exit(0)

        if oper == 1:
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

        elif oper == 2:
            
            print("We had {} passengers with missing cabin".format())
            print("We have {} passengers with proper cabin".format())

        elif oper == 3:
            
            print("We had {} passengers with missing age".format())
            print("We have {} passengers with proper age".format())
            print("Average age of all {} passengers was {} years".format())

        elif oper == 0:
            break

        else:
            break

main()
