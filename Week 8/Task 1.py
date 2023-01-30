import math, random

def menu():
    print("What do you want to do:\n1) Calculate the area of the circle\n2) Guess the number\n0) Stop")
    action = int(input("Your choice:\n"))
    return action

def main():
    print("This program uses libraries to solve tasks.")

    while True:
        oper = menu()

        if oper == 1:
            r = int(input("Enter the radius of the circle as an integer:\n"))
            area = math.pi * math.pow(r, 2)
            print("With a radius of {}, the area of the circle is {}.\n".format(r, "{:.2f}".format(area)))

        elif oper == 2:
            print("Guess the integer drawn by the program.")
            count = 1
            random.seed(1)
            number = random.randint(0, 1000)
            
            while True:
                guess = int(input("Enter an integer between 0 and 1000:\n"))
                
                if guess > number:
                    print("The requested number is lower.")
                    count = count + 1
                elif guess < number:
                    print("The requested number is higher.")
                    count = count + 1
                else:
                    print("Correct! You used {} tries to guess the correct integer..\n".format(count))
                    break

        else:
            break

main()
