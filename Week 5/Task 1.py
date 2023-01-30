def phase_one():
    print("Phase one:\nNow we are in 'print_to_screen' function.\nThis function prints only text.\n")
phase_one()
    
print("Phase two:")
i = int(input("Enter an integer:\n"))
print("At the main level, before the subprogram, the number is", i)
def phase_two(x):
    print("In the function, the value of the parameter is", x)
    print("In the function, the value of the parameter after squaring is", x**2)
phase_two(i)
print("At the main level, after the subprogram, the number is", i, "\n")
print("Phase three:")
f = input("Enter first name:\n")
l = input("Enter last name:\n")
def phase_three(x, y):
    print("The first name '%s' and the last name '%s' form the name '%s'."%(x,y, x +" "+ y))
phase_three(f, l)
