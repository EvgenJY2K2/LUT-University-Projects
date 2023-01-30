a = int(input("Enter the value for a:\n"))
b = int(input("Enter the value for b:\n"))

while a < b or a > 10000 or b > 10000:
    print("a: %s; b: %s"%(a,b))
    a = a*2
    b = b + 100
    continue
print("a: %s; b: %s"%(a,b))
