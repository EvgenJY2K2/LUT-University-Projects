i = int(input("Enter an integer: \n"))
if i < 0:
    print("Number is less than 0.")
elif i > 0 and i < 10:
    print("The number is less than 10.")
else:
    print("The number is greater than or equal to 10.")

if i % 2 == 0:
    print("The number you entered is even.")

else:
    print("The number you entered is odd.")
