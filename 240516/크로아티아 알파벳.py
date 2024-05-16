alphabet_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for alphabet in alphabet_list:
    word = word.replace(alphabet, "?")
print(len(word))