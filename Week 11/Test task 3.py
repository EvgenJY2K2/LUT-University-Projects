n = int(input("Give a nonnegative integer:\n"))

def Fibo(n):
    if n == 0:    
       return n
    elif n == 1 or n == 2:    
       return 1
    else:    
       return Fibo(n-1) + Fibo(n-2)   

print("Fibo({}) returns {}".format(n, Fibo(n+1)))
