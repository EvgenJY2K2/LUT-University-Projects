n = int(input("Input an integer:\n"))
m = 1
while True:
    m = m + 1
    if abs(n - m**2) == 0:
        print("Integer square root is", m)
        break
    else:
        d = n-m**2
        if d > m:
            continue
        else:
            print("Integer square root is", m)
            break
