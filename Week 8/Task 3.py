from datetime import datetime, timedelta

def menu():
    print("What do you want to do:\n1) Identify the components of a time object\n2) Calculate age in days\n3) Print the days of the week\n4) Print the months\n0) Stop")
    action = int(input("Your choice:\n"))
    return action

def main():
    print("This program uses the datetime library to deal with time.")

    while True:
        oper = menu()

        if oper == 1:
            dt = input("Enter the date and time in the format 'dd.mm.yyyy hh:mm':\n")
            date = datetime.strptime(dt, '%d.%m.%Y %H:%M')
            print("You gave year", date.strftime("%Y"))
            print("You gave month", date.strftime("%m"))
            print("You gave day", date.strftime("%d"))
            print("You gave hour", date.strftime("%H"))
            print("You gave minute", date.strftime("%M"))
            print("")

        elif oper == 2:
            bd = input("Enter your birthday as dd.mm.yyyy:\n")
            bd_date = datetime.strptime(bd, '%d.%m.%Y')
            datum = datetime.strptime("01.01.2022", '%d.%m.%Y')
            old = datum - bd_date
            print("On January 1, 2022, you were {} days old.\n".format(old.days))

        elif oper == 3:
            start = datetime.strptime("31.10.2022","%d.%m.%Y")
            delta = timedelta(days = 1)
            for i in range (7):
                print(start.strftime("%A"))
                start = start + delta
            print("")
            
        elif oper == 4:
            start = datetime.strptime("01.01.2022","%d.%m.%Y")
            delta = timedelta(days = 31)
            for i in range (12):
                print(start.strftime("%b"))
                start = start + delta
            print("")
        else:
            break
main()
