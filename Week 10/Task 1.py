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
        print("Error while processing file '{}', exiting.".format(file))
        sys.exit(0)

    return file_list 

def write(file, cars_dict, cars, f_list):
    try:
        f_write = open(file, "w")
        f_write.write("{} car brands and {} cars were identified:\n".format(len(cars), len(f_list)))
        for key, value in cars_dict.items(): 
            f_write.write('{}: {} cars\n'.format(key, value))

        f_write.close()
    except:
        print("Error while processing file '{}', exiting.".format(file))
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
    f_read = input("Enter the name of the file to be read:\n")
    f_write = input("Enter the name of the file to be written:\n")
    
    f_list = read(f_read)
    cars = brands(f_list)
    car_dict = {}
    count = 0
    for car in cars:
        car_dict[car] = f_list.count(car)

    if len(cars) != 0:
        print("{} car brands and {} cars were identified:".format(len(cars), len(f_list)))

        write(f_write, car_dict, cars, f_list)

        for key, value in sorted(car_dict.items()):
            print('{}: {} cars'.format(key, value))
    else:
        print("The file was empty, no car brand was recognized.")

main()
