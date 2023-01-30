rows = int(input("Enter number of rows:\n"))
for x in range(0, rows):
    for j in range(rows-x-1):
        print("  ", end="")
    for k in range(2*x+1):
        print("* ", end = "")
    print()
