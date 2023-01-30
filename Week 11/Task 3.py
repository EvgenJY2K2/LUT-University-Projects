n = int(input("Give a nonnegative integer:\n"))

def Fibo(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return (Fibo(n-1) + Fibo(n-2))
print("Fibo({}) returns {}".format(n, Fibo(n)))
