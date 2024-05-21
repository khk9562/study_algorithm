N, B = map(int, input().split())
result = ""

while N > 0:
    나머지 = N % B

    if 나머지 >= 10:
        # 아스키코드상으로 65가 A
        result += chr(55 + 나머지)
    else:
        result += str(나머지)
    N = N // B

print(result[::-1])
