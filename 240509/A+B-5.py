# 입력의 마지막에는 0 두 개가 들어온다.
# 바본가? 문제를 제대로 읽자....
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
