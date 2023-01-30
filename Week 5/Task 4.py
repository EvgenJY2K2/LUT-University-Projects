def ask_for_string():
    string = input("Enter a string, 5-15 characters:\n")
    return string

def count_length(st):
    count = 0
    for i in st:
        count = count + 1
    return count

def main():
     while True:
         
        out = ask_for_string()
        if count_length(out) < 5:
            print("Too short, %s characters, please enter a new one."%count_length(out))
        elif count_length(out) > 15:
            print("Too long, %s characters, please enter a new one."%count_length(out))
        else:
            print("The length of the string is good, %s characters."%count_length(out))
            print("Bye.")
            break
main()
