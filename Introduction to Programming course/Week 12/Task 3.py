import random, string
print("Welcome to password generator.")
def menu():
    print("0) Exit\n1) Password with letters\n2) Password with digits\n3) Password with letters & digits\n4) Password with letters, digits & special characters")
    action = int(input("Select password type:\n"))
    return action
def main():
    random.seed(8292)
    while True:
        try:
            choise = menu()
        except:
            print("Invalid choise. Please try again.\n")
            continue
        if choise == 1:
            length = int(input("Input password length:\n"))
            letters = string.ascii_letters
            result_str = ''.join(random.choice(letters) for i in range(length))
            print(result_str)

        elif choise == 2:
            length = int(input("Input password length:\n"))
            digits = string.digits
            result_dig = ''.join(random.choice(digits) for i in range(length))
            print(result_dig)

        elif choise == 3:
            length = int(input("Input password length:\n"))
            letters = string.ascii_letters
            digits = string.digits
            result_char = ''.join(random.choice(letters + digits) for i in range(length))
            print(result_char)

        elif choise == 4:
            length = int(input("Input password length:\n"))
            special_chars = string.punctuation
            letters = string.ascii_letters
            digits = string.digits
            result_char = ''.join(random.choice(letters + digits + special_chars) for i in range(length))
            print(result_char)
        else:
            break
main()
            
