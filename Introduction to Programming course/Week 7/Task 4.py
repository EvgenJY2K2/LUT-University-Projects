info_list = []
car_list = []


class Car:
    brand = ""
    price = 0

def create_car(list):
    Car.brand = list[0]
    Car.price = list[1]
    car_list.append(Car.brand)
    car_list.append(Car.price)

    return car_list

def cars_print(list_f):
    print("{} {}".format(list_f[0],list_f[1]))
    print("{} {}".format(list_f[2],list_f[3]))
    print("{} {}".format(list_f[4],list_f[5]))
    
    
def main():
    print("This program adds car information to the list and prints them.")

    while True:
        print("Available functions:\n1) Enter the car information\n2) Print the details of the cars\n0) Stop")
        oper = int(input(("Your selection:\n")))
        
        if oper == 1:
               brand = input("Enter the brand of the car:\n")
               price = int(input("Enter the price of the car:\n"))
               print("")
               info_list.append(brand)
               info_list.append(price)
               create_car(info_list)
               info_list.clear()

        elif oper == 2:
            print("The list includes the following car brands and prices:")
            cars_print(car_list)
            print("")

        elif oper == 0:
            break

        else:
            print("Unknown selection")


main()
