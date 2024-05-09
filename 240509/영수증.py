# 총 금액
X = int(input())
# 구매한 물건의 종류의 수
N = int(input())
calc = 0

for i in range(N):
# 각 물건의 가격 a와 개수 b
    a, b = map(int, input().split())
    calc += a * b

if X == calc:
    print("Yes")
else:
    print("No")