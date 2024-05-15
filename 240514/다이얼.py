# 입력 받은 단어
word = input()

# 알파벳에 따른 다이얼 숫자와 걸리는 시간을 매핑한 딕셔너리
alphabet_list = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
}

# 총 시간을 계산
total_time = 0
for char in word:
    for key in alphabet_list:
        if char in alphabet_list[key]:
            # 다이얼 숫자에 1을 더해 시간을 계산 (예: 2 -> 3초, 3 -> 4초 ...)
            total_time += key + 1
            break

print(total_time)
