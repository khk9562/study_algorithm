# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어

word = input()
reversed_word = word[::-1]

if word == reversed_word: print(1)
else : print (0)