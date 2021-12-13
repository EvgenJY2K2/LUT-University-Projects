```
import numpy as np

#Receive input for dimentions and check if valid
try:
  a = int(input("Enter the dimentions for the square matrices: "))
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

#Generate the matrices
for i in range (num):
  M = np.random.randint(el, size = (a, a))
  #Invert the matrices
  M_vert = np.linalg.inv(M)
```
