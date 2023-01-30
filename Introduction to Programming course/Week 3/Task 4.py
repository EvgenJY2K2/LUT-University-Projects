x = input("Enter word 1:\n")
y = input("Enter word 2:\n")


if y > x:
    print("'%s' is earlier in the alphabet than '%s'."%(x, y))
else:
    print("'%s' is earlier in the alphabet than '%s'."%(y, x))
if "z" in x:
    print("Letter 'z' is found in word 1.")
if "z" in y:
    print("Letter 'z' is found in word 2.")
else:
    print("The letter 'z' was not found in either word.")

t = input("Enter the word to be tested:\n")
w = ""
for i in t:
    w = i + w
if (t == w):
    print("The word you entered '%s' is a palindrome."%t)
else:
    print("The word you entered is not a palindrome.")
    print("The inverted form of it is '%s' and it is different from input '%s'."%(w, t))
