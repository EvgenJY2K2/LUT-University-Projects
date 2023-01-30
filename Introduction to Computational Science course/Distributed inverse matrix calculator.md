```
#IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt

'''
    Duties: the program generates and computes inverse of square matrices
    using parallel distribution. 
    The minimum number of matrices is 10000.
    The matrices have at least 20000 elements on the diagonal with 
    no limits on the values range. 
    
    :param a: the dimentions of the square matrices (min 20000)
    :type a: int
    
    :param el: the range of the values for the matrices
    :type el: int
    
    :param num: the number of matrices to be generated (min 10000)
    :type num: int

    :return: stores generated and inverted matrices in a list.
    Each of the generated matrices are followed by their inverses.
    Displays plots of the first three matrixes from both lists.
'''  

#PREPARE AND CHECK INPUTS 
#Receive input for dimentions and check if valid
try:
  a = int(input("Enter the dimentions of the square matrices: "))
except:
  print('Error: Please enter integer value.')

while True:
   if a < 20000:
     print('Error: Please enter value bigger than 20000.')
     a = int(input("Enter the dimentions for the square matrices: "))
   else:
     break

#Receive input for value range and check if valid
try:
  el = int(input("Enter the range of the values for the matrices: "))
except:
  print('Error: Please enter integer value.')

#Receive input for number of matrixes to be generated
try:
  num = int(input("Enter the number of matrices to be generated: "))
except:
  print('Error: Please enter integer value.')

while True:
  if num < 10000:
    print('Error: Please enter number bigger than 10000.')
    num = int(input("Enter the number of matrices to be generated: "))
  else:
    break

#PREPARE ARGUMENTS
results = list()

call_arguments = []
for i in range(num):
    M = np.random.randint(el, size = (a, a))
    call_arguments.append(M)

#DEFINE MAIN SOLVER FUNCTION
def solver(argument_set):
    M = argument_set
    M_vert = np.linalg.inv(M)
    return M_vert

#SOLVE PROBLEM
processed_results = []
for argument_set in call_arguments:
    invert_results = solver(argument_set)
    processed_results.append(invert_results)

#POST PROCESSING
for argument_set, result_set in zip(call_arguments, processed_results):
    M = argument_set
    M_vert = result_set
    results.append([M, M_vert])

print(results)

#MATRICES VISUALIZATION 
print()

#DEFINE PLOTTING FUNCTIONS
def plot(i=3):
    #Plot the generated matrices
    print("Plots of first 3 generated matrixes: ")
    for i in range(i):
        plt.matshow(call_arguments[i])
        plt.colorbar()
        plt.show()

    #Plot the inverted matrices
    print("Plots of first 3 inverted matrixes: ")
    for i in range(i+1):
        plt.matshow(processed_results[i])
        plt.colorbar()
        plt.show()

plot()
```
