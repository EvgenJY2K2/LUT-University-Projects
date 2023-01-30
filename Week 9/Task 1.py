import sys
def read(file):
    count = 0
    file_list = []

    try:
        read = open(file, "r")
        lines = read.readlines()
        for line in lines:
            check = int(line)
            count = count + 1
            file_list.append(line)
        print("File '{}' read successfully, {} lines.".format(file, count))
    except:
        print("Error while processing file '{}', stopping.".format(file))
        sys.exit(0)

    return file_list 

def write(file, list):
    try:
        f_write = open(file, "w")
        for i in list:
            f_write.write(i)
        print("File '{}' was successfully written.".format(file))
    except:
        print("Error processing file '{}', stopping.".format(file))
        sys.exit(0)

def main():
    f_read = input("Enter the name of the file to be read:\n")
    f_list = read(f_read)

    f_write = input("Enter the name of the file to be written:\n")
    write(f_write, f_list)

main()
