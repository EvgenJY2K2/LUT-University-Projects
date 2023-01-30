import itertools
string = input("Give a string whose permutations you want to print:\n")
nums = list(string)
permutations = list(itertools.permutations(nums))
ans = []
for permutation in permutations:
    ans.append(''.join(permutation))
separator = ", "
print("Permutations of the string {} are: {}.".format(string, separator.join(ans)))
