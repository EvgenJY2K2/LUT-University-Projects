l = int(input("Enter the lower limit of the range:\n"))
u = int(input("Enter the upper limit of the range:\n"))

e = True

while e:
    for i in range(l, u+1):
        if i%5 == 0 and i%7 == 0:
            print("The number %s is divisible by 5 and 7."%i)
            print("Stopping the search.")
            e = False
            break
        elif i%5 != 0:
            print("%s is NOT divisible by 5."%i)
            continue
        elif i%7 != 0:
            print("%s is NOT divisible by 7."%i)
            continue
        i = i + 1
    else:
        print("No suitable value was found in the range.")
        e = False
    
