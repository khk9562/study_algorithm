# 문제 풀이
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c or b == c:
    if a == b:
        print(1000 + 100 * a)
    elif a == c:
        print(1000 + 100 * a)
    else:
        print(1000 + 100 * b)
elif a != b != c:
    print(max(a, b, c) * 100)