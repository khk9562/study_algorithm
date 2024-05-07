import math

# 테스트 케이스의 수를 입력받습니다.
t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 점 사이의 거리를 계산합니다.
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 두 원이 일치하는 경우
    if distance == 0 and r1 == r2:
        print(-1)
    # 두 원이 내접하거나 외접하는 경우
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    # 두 원이 서로 다른 두 점에서 만나는 경우
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    # 그 외 모든 경우, 즉 두 원이 만나지 않는 경우
    else:
        print(0)
