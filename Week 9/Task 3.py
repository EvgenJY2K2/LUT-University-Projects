import sys

def read(file):
    count = 0
    file_list = []

    try:
        read = open(file, "r")
        lines = read.readlines()
        for line in lines:
            file_list.append(line.strip())
    except:
        print("The file was empty, no car brand was recognized.")
        sys.exit(0)

    return file_list 

def write(file, list):
    try:
        f_write = open(file, "w")
        for i in list:
            f_write.write(i + "\n")
    except:
        print("Error processing file '{}', stopping.".format(file))
        sys.exit(0)

def brands(list):
    brands = []
    for car in list:
        if car not in brands:
            brands.append(car)
        else:
            continue
    return brands

def main():
    f_read = input("Give the name of the file to read:\n")
    f_write = input("Give the name of the file to write:\n")
    
    f_list = read(f_read)
    cars = brands(f_list)

    write(f_write, cars)

    if len(cars) != 0:
        print("There were {} different car brands in the file.".format(len(cars)))
        for car in cars:
            print(car)
    else:
        print("The file was empty, no car brand was recognized.")

main()
