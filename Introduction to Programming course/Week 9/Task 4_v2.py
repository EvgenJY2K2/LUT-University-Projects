import csv, sys

def menu():
    print("You can do the following\n1) Calculate passengers with missing ages\n2) Calculate passengers without a cabin\n3) Calculate average age of passengers (skip missing ages)\n0) Exit")
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

    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)
    
    rows = []
    for row in csvreader:
        rows.append(row)

    print("The file contains {} passengers\n".format(len(rows)))

    while True:
        oper = menu()

        try:
            oper = int(oper)
        except:
            print("Faulty user input. Exiting.")
            sys.exit(0)

        if oper == 1:
            missing = 0
            proper = 0
            
            for item in rows:
                try:
                    age = float(item[5])
                    proper = proper + 1
                except:
                    name = item[3]
                    print("{} was missing age".format(name))
                    missing = missing + 1

            print("We had {} passengers with missing age".format(missing))
            print("We have {} passengers with proper age\n".format(proper))

        elif oper == 2:
            missing = 0
            proper = 0

            for item in rows:
                if not item[10]:
                    name = item[3]
                    print("{} was missing cabin".format(name))
                    missing = missing + 1
                else:
                    proper = proper + 1
            
            print("We had {} passengers with missing cabin".format(missing))
            print("We have {} passengers with proper cabin\n".format(proper))

        elif oper == 3:

            ages = []
            missing = 0
            proper = 0
            sum_age = 0
            
            for item in rows:
                try:
                    age = float(item[5])
                    ages.append(age)
                    proper = proper + 1
                except:
                    name = item[3]

                    print("{} was missing age".format(name))
                    missing = missing + 1
            for age in ages:
                sum_age = sum_age + age
            average = round(sum_age/len(ages))
            
            print("We had {} passengers with missing age".format(missing))
            print("We have {} passengers with proper age".format(proper))
            print("Average age of all {} passengers was {} years\n".format(proper, average))

        elif oper == 0:
            break

        else:
            break

main()
