x = int(input("Enter the first number:\n"))
y = int(input("Enter the second number:\n"))

print("The calculator can perform the following operations:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Exponentiation")
print("The numbers you entered are %s and %s"%(x, y))
f = int(input("Select function (1-5):\n"))

if f == 1:
    print("Addition: %s + %s ="%(x,y), x+y)
elif f == 2:
    print("Subtraction: %s - %s ="%(x,y), x-y)
elif f == 3:
    print("Multiplication: %s * %s ="%(x,y), x*y)
elif f == 4:
    if y == 0:
        print("Error: Zero cannot be used as a divisor.")
    else:
        print("Division: %s / %s ="%(x,y), round((x/y), 2))
elif f == 5:
    print("Exponentiation: %s**%s ="%(x,y), x**y)
else:
    print("The operation was not recognized.")
