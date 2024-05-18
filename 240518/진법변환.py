N, B = input().split()
B = int(B)
result = 0

for n in N:
    # 숫자인 경우
    if n.isdigit():
        val = int(n)
    else:
        val = ord(n) - ord('A')  + 10
    result = result * B + val

print(result)
