s = int(input("Enter the starting value:\n"))
f = int(input("Enter the ending value:\n"))

print("Implementation with a for loop:")
for i in range(s, f+1):
    print(i, end = ' ')
print("\n")
print("Implementation with a while loop:")
while s <= f:
    print(s, end = ' ')
    s = s+1
