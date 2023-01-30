e = True

while e:
   print("This calculator can perform the following functions:\n1) Enter numbers\n2) Sum\n3) Subtract\n4) Multiplication\n5) Division\n6) Power of\n0) Stop")
   f = int(input("Select function (0-6):\n"))

   if f < 0 or f > 6:
       print("Unknown selection, try again.")
       continue 
   if f == 1:
       x = int(input("Enter the first number:\n"))
       y = int(input("Enter the second number:\n"))
       print("You entered numbers %s and %s"%(x, y))
       continue
   elif f == 2:
       print("Sum %s + %s ="%(x,y), x+y)
   elif f == 3:
       print("Subtraction %s - %s ="%(x,y), x-y)
   elif f == 4:
       print("Multiplication %s * %s ="%(x,y), x*y)
   elif f == 5:
       if y == 0:
           print("Cannot divide by zero.")
           continue
       else:
           print("Division %s / %s ="%(x,y), round((x/y), 2))
   elif f == 6:
       print("Power of %s**%s ="%(x,y), x**y)
   else:
       print("Stopping")
       print("Bye")
       e = False
