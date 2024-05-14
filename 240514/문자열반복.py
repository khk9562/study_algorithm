# 테스트 케이스 개수
T = int(input())
# 각 문자(S 문자열 내 문자)를 R번 반복해 출력
for i in range(T):
    R, S = map(str, input().split(" "))
    R = int(R)
    for s in S:
        print(s * R, end='')
    # T 개수만큼 엔터 쳐서 출력되어야 하므로
    print()

