import sys
n = len(sys.argv)

print("The even numbers of the input are the following:")
for i in range(1, n-1):
    if int(sys.argv[i])%2 == 0:
        print(sys.argv[i],  end = " ")

print()

sum = 0
count = 0
for i in range(1, n-1):
    if int(sys.argv[i])%2 == 0:
        sum = int(sys.argv[i]) + sum
        count = count + 1
average = sum/count
print("Average of the numbers is %.2f." % average)
