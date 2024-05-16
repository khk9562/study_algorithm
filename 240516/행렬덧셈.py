N, M = map(int, input().split())
# N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
A = []
B = []

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# print("A", A)
# print("B", B)

result = []
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()