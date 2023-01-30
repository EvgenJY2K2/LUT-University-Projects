file_name = input("Enter the name of the file to be read:\n")

file = open(file_name,"r", encoding="utf-8")

line = file.readlines()
count_name = 0
count_char = 0
for i in line:
    count_name +=1
    i.strip()
    for x in i:
        count_char +=1
print("The file contained {} names and {} characters.".format(count_name, count_char))
print("The average name length was {} characters.".format(round(count_char/count_name - 1)))



