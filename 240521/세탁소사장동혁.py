
# 쿼터 0.25
# 다임 0.10
# 니켈 0.05
# 페니 0.01

T = int(input())

for _ in range(T) :
    C = int(input())
    # C의 단위는 센트이고, 1달러 = 100센트
    쿼터 = C // 25
    다임 = (C % 25) // 10
    니켈 = ((C % 25) % 10) // 5
    페니 = ((C % 25) % 10) % 5
    print(f"{쿼터} {다임} {니켈} {페니}")