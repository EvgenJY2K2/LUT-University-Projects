file_name = input("Enter the name of the file containing the data:\n")
out_name = input("Enter the name of the file to be saved:\n")
in_file = open(file_name,"r")

def total_num(file):
    total = 0 
    file = open(file,"r")
    line = file.readlines()
    for i in line:
        total = total + int(i)
    return total

def small_num(file):
    file = open(file,"r")
    line = file.readlines()
    min_num = int(line[0])
    for i in line:
        if int(i) < min_num:
            min_num = int(i)
        else:
            continue
    return min_num

def larg_num(file):
    file = open(file,"r")
    line = file.readlines()
    max_num = int(line[0])
    for i in line:
        if int(i) > max_num:
            max_num = int(i)
        else:
            continue
    return max_num

out_file = open(out_name, "w")
out_file.write("The smallest number of steps was {} steps.\n".format(small_num(file_name)))
out_file.write("The largest number of steps was {} steps.\n".format(larg_num(file_name)))
out_file.write("There were {} steps in total.".format(total_num(file_name)))
out_file.close()

print("The smallest number of steps was {} steps.".format(small_num(file_name)))
print("The largest number of steps was {} steps.".format(larg_num(file_name)))
print("There were {} steps in total.".format(total_num(file_name)))
