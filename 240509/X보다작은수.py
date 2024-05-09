N, X = map(int, input().split())
A = list(map(int, input().split()))

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")