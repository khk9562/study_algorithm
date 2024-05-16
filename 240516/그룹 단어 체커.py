N = int(input())
count = 0

for i in range(N):
    # 총 N개의 문자열인 단어를 차례로 입력받는다.
    word = input()
    # print("word",word)
    # 이전 문자를 저장
    prev = ""
    isGroupWord = True

    for j in word:
        # prev에 이미 해당 문자가 들어있고, prev 마지막 문자 즉 직전에 나온 문자가 현재 문자와 다르다면 그룹 단어가 아님
        if j in prev and prev[-1] != j:
            isGroupWord = False
            break
        prev += j
        # print("prev", prev)
        
    if isGroupWord:
        count += 1

print(count)


