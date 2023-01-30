def rep(text, num):
    for i in range(num):
        print(text)
    print("")

while True:
    t = input("Enter text:\n")
    if t == 'quit':
        print("Bye.")
        break
    i = int(input("Enter an integer:\n"))
    rep(t, i)
    
