import fractions

print("Give the first fraction.")
num1 = int(input("Give numerator (top):\n"))
den1 = int(input("Give denominator (bottom):\n"))
f = fractions.Fraction(num1, den1)

print("Give the second fraction.")
num2 = int(input("Give numerator (top):\n"))
den2 = int(input("Give denominator (bottom):\n"))
s = fractions.Fraction(num2, den2)

exp  = int(input("Give an exponent:\n"))

print("Sum: {}/{} + {}/{} = {}".format(num1, den1, num2, den2, f+s))
print("Subtract: {}/{} - {}/{} = {}".format(num1, den1, num2, den2, f-s))
print("Multiply: ({}/{}) * ({}/{}) = {}".format(num1, den1, num2, den2, f*s))
print("Divide: ({}/{}) / ({}/{}) = {}".format(num1, den1, num2, den2, f/s))
print("Power: ({}/{})**3 = {}".format(num1, den1, f**exp))
