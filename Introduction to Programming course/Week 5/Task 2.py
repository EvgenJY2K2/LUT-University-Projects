f = int(input("Enter the first integer:\n"))
s = int(input("Enter the second integer:\n"))

def test(x, y):
    if x > y:
        print("%s is greater than %s"%(x, y))
        return x
    elif x < y:
        print("%s is greater than %s"%(y, x))
        return y
    else:
        print("The integers are the same.")
        return x

big = test(f, s)

t = int(input("Enter the integer that is subtracted from the larger:\n"))

def sub(i, sm):
    new = big - i
    test(new, sm)
sub(t, s)

