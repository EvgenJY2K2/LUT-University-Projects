PII =  3.14

x = int(input("Enter a positive integer: \n"))
print("Number",x,"multiplied by itself is", x*x)

r = int(input("Give the radius of a circle as an integer: \n"))
print("The radius of the circle is %s, the circumference is %s and the area is %s."%(r, 2*PII*r, PII*(r**2)))

a = int(input("Enter the length of one side of the rectangle as an integer: \n"))
b = int(input("Enter the length of another side of the rectangle as an integer: \n"))
print("The sides of the rectangle are %s and %s; perimeter is %s; and the area is %s."%(a, b, 2*(a+b), a*b))
