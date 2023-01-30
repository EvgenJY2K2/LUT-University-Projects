def menu():
    print("This calculator can perform the following functions:\n1) Enter the values\n2) Sum\n3) Divide\n0) Stop")
    operation = int(input("Select the function (0-3):\n"))
    return operation

def sum(value1, value2):
    sum = value1 + value2
    return "sum " + str(value1) + " + " + str(value2) + " = " + str(sum) + "\n"

def division(value1, value2):
    if value2 == 0:
        return ("You cannot divide by zero.")
    else:
        div = round((value1/value2), 2)
        return "Division " + str(value1) + " / " + str(value2) + " = " + str(div) + "\n"

def read_value(file, count):
    file = open(file,"r")
    line = file.readlines()
    if count > 5:
        print("End of values, end the program." )
        return 0
    else:
        value = int(line[count])
        return value
    
def main():
    file_name = input("Enter the name of the file to read:\n")
    in_file = open(file_name,"r")
    out_file = open("Exercise5_output.txt", "w")
    val_count = 0

    while True:
        action = menu()

        if action < 0 or action > 3:
            print("Unknown choice, try again.")
            continue

        if action == 1:
            x = read_value(file_name, val_count)
            val_count = val_count + 1
            y = read_value(file_name, val_count)
            val_count = val_count + 1
            print("Values {} and {} were read".format(x, y))
            continue

        elif action == 2:
            out_file.write(sum(x, y))
            print("Result saved in file.")

        elif action == 3:
            out_file.write(division(x, y))
            print("Result saved in file.")
            
        else:
            print("Stopping")
            break
    out_file.close()
main()
