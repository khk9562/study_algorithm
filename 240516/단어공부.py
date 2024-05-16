# 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
# 그게 여러개면 ? 출력
word = input().upper()
word_list = list(word)
dict = {}

for item in word_list:
    if item in dict:
        dict[item] += 1
    else:  
        dict[item] = 1

result =[k for k,v in dict.items() if v == max(dict.values())]

if len(result) == 1:
    print(result[0])
else: print("?")