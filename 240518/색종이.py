# 색종이의 수
N = int(input())

# 바둑판 바둑 놓듯이 생각하기
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    
    # 색종이가 차지하는 부분을 1로 표시
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = sum(row.count(1) for row in arr)
print(result)
