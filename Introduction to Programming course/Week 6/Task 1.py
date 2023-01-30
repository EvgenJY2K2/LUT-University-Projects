def file_write(ref):
    file = open(ref, "w")
    while True:
        name = input("Enter a name to save to the file (0 to stop):\n")
        if name == "0":
            break
        else:
            name1="{}\n".format(name)
            file.write(name1)
            continue
    file.close()
            
def file_read(file):
    verif = open(file, "r")
    lines = verif.readlines()
    print("The following names are stored in the file '{}':".format(file))
    for i in lines:
        print(i.strip())
    verif.close()

file_name = input("Enter the name of the file to be saved:\n")
file_write(file_name)
file_read(file_name)
