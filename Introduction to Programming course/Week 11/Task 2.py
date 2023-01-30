m = int(input("Input the amount of months:\n"))

n1 = 0
n2 = 1
for i in range(m):
    nth = n1 + n2
    n1 = n2
    n2 = nth
print("After {} months, there will be {} rabbit couples.".format(m, nth))
