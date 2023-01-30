shop = []

while True:
    print("Your shopping list contains the following products:\n{}".format(shop))
    print("You can choose from the functions below:\n1) Add\n2) Remove\n0) End")
    oper = int(input(("Your choice:\n")))

    if oper == 1:
               item = input("Enter the product to be added:\n")
               shop.append(item)
               print("")

    elif oper == 2:
        print("You have  {}  items in your shopping list.".format(len(shop)))
        rm = int(input("Enter the location of the product to be removed:\n")) - 1
        shop.remove(shop[rm])
        print("")

    elif oper == 0:
        print("You did not buy the following products:\n{}".format(shop))
        break

    else:
        print("Unknown selection")
