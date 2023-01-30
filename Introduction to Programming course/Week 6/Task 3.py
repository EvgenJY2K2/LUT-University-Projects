file_name = input("Enter the name of the file to be read:\n")
in_file = open(file_name,"r", encoding="utf-8")

out_file = open("Palindromes.txt", "w")

line = in_file.readlines()
for i in line:
    for word in i.split():
        l_word = word.lower()
        w = ""
        for i in l_word:
            w = i + w
        if (l_word == w):
            out_file.write(word + "\n")
            print("row '{}' is a palindrome.".format(word))
        else:
            print("row '{}' is not a palindrome.".format(word))
