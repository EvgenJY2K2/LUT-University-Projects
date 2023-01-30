import time
import sys

def search_function(filename):
    values = ["",""]
    values[0] = 0  # Smaller number is saved here
    values[1] = 0  # The greater number is saved here

    try:
        read = open(filename, "r")
    except:
        print("Error while processing file '{}', stopping.".format(filename))
        sys.exit(0)

    lines = read.readlines()
    file_list = []
    i = 0

    for line in lines:
        file_list.append(int(line))

    for value in range(len(file_list)):
        try:
            first = file_list[i]
            second = file_list[i+1]
        except:
            values[0] = 0
            values[1] = 0

        if first < second/3:
            values[0] = first
            values[1] = second
        else:
            i = i + 1
            continue

    return values

def main():
    file = input("Input filename: \n")
    timer1 = time.perf_counter()
    result = search_function(file)
    timer2 = time.perf_counter()
    duration = timer2 - timer1
    if ((result[0] == 0) and (result[1] == 0)):
        print("Search algorithm did not find a matching pair.")
    elif (duration > 2):
        print("Search algorithm was not fast enough.")
    else:
        print("Search algorithm was fast! Awesome!")
        print("It found a matching pair:", result[0], "and", result[1])

main()
