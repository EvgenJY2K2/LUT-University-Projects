x = input("Enter a long word: ")
l = len(x)
print("The first five letters of the word you entered are:", x[:5])
print("The last five letters are:", x[l-5:])
print("Letters 2, 3, 4 and 5 are:", x[1:5], "\n")

print("Every second letter of the word starting with the second letter:", x[1::2], "\n")
print("You entered the word \'%s\' which is backwards \'%s\'."%(x, x[l::-1]), "\n")

s = int(input("Enter start index: "))
e = int(input("Enter end index: "))
t = int(input("Enter step: "))
print("With these values \'%s\' produces this: %s"%(x, x[s:e:t]), "\n")

print("Your word is",l,"characters long.")
