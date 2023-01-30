class Car:
    brand = ""
    amount = 0

def ask_details(x):
    if x == "brand":
        br = input("Give the car brand:\n")
        Car.brand = br
        return br
    else:
        num = int(input("Give the number of car brands in stock:\n"))
        Car.amount = num
        return num

def main():
    b = ask_details("brand")
    n = ask_details("num")
    print("There are currently {} {} cars in stock.".format(n, b))

main()
main()
