from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

S = input()

for item in alphabet_list:
    print(S.find(item), end=' ')

