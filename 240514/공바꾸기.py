# 문제: 공 바꾸기
# 1. N개의 바구니, 각각의 바구니에 1부터 N번까지 번호가 매겨져있음
# 2. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음
# 3. 앞으로 M번 공을 바꿀 계획
# 4. 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 바꿈
# 5. 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후 각 바구니에 어떤 공이 들어있는지 구하기

# 풀이
N, M = map(int, input().split())
arr = []
for index in range(N):
    arr.append(index+1)
for index in range(M):
    i,j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
print(" ".join(str(a) for a in arr))