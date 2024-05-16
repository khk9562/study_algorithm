N = int(input())

# 상단 삼각형
for i in range(1, N+1):
    print(" " * (N - i) + "*" * (2 * i - 1))
# 하단 삼각형
for i in range(N-1, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))
