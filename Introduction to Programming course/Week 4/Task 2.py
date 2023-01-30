count = 0
sum = 0.00
while True:
    x = int(input("Enter a course grade between 1-5 (-1 stops):\n"))

    if x == 0 or x < -1 or x > 5:
        print("Incorrect input. Only grades 1-5 are valid (-1 stops).")

    elif x != -1:
        sum = sum + x
        count += 1
        continue
            
    else:
        avg = sum / count
        print("The average grade is %.1f." % avg)
        break
