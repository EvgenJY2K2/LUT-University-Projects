x = input("Do you want to stop the execution of the program (y/Y): \n")
if x == "y" or x == "Y":
    print("Thank you for using the program.")
else:
    u = input("Enter username: \n")
    p = input("Enter password: \n")
    if u == "Matt" and p == "password":
        print("User recognized.")
    else:
        print("The login name you entered was %s characters long, but you entered an invalid login name or password."%(len(u)))
                            
                        
