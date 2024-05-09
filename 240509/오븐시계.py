# 문제풀이
# 현재 시각 a시 b분
# 요리에 필요한 시간 c(분)
a, b = map(int, input().split())
c = int(input())

# 분 추가
b += c
# 추가된 분으로 시 계산
a += b // 60
# 분은 60으로 나눈 나머지
b = b % 60
# 시가 24를 넘어가면 24로 나눈 나머지
a = a % 24

print(f"{a} {b}")
