print("This program calculates the average of the 3 numbers you enter.")
x = float(input("Enter the first number: \n"))
y = int(input("Enter the second number: \n"))
z = float(input("Enter the third number: \n"))

print("The sum of the numbers you entered is %s."%(x+y+z))
print("Average rounded to 3 decimal places is %s."%(round(((x+y+z)/3), 3)))
print("Average as an integer without decimal part %s."%(int((x+y+z)/3)))
