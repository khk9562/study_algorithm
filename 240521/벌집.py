# 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산

N = int(input())
count = 0
x=1
for i in range(N):
    x += 6*i 
    count += 1
    if x >= N:
        break
print(count)
