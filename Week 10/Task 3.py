import numpy as np
print("This program demonstrates use of numpy-matrix.")
row = int(input("Enter amount of rows:\n"))
col = int(input("Enter number of columns:\n"))

print("Zero-matrix of the given rows & columns is:\n", np.zeros((col, row), dtype=int))
z_array = np.zeros((col, row), dtype=int)

array = np.arange(col * row).reshape(row, col)

print("Matrix printed with np-formatting:")

n_sorted = []
row_index = 0
for rows in z_array:
    column_index = 0
    for item in rows:
        item = (row_index + 1)*(column_index + 1)
        z_array[row_index][column_index] = item
        column_index = column_index + 1
        n_sorted.append(item)
    row_index = row_index + 1
print(z_array, '\n')
print("Matrix sorted into one array:")
print(np.sort(z_array, axis=None))
print("Matrix printed with elements separated by semicolons:")
for rows in z_array:
    print("{};{};{};{};".format(rows[0], rows[1], rows[2], rows[3]))
print("")
    
while True:
    try:
        print("Shaping the matrix. Please, enter the new dimensions.")
        nrow = int(input("Enter amount of new rows:\n"))
        ncol = int(input("Enter amount of new columns:\n"))
        reshape = z_array.reshape(nrow,ncol)
    except:
        print("Faulty shape. Please, try again.")
        continue
    else:
        break

print("Newly shaped matrix is:\n", reshape)

line = np.sort(z_array, axis=None)
print("Largest number in the matrix is:", max(line))
print("Smallest number in the matrix is:", min(line))
print("Sum of all values in the matrix is:", sum(line))
list_values=[int(item) for item in input("Enter the list items:\n").split()]
np_list = np.array(list_values)
print("Unique values are:", np.unique(np_list))
