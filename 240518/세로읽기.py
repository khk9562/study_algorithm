arr = []
# 행 개수
row_count = 0
col_count = 0
while True:
    try :
        li = list(input())
        arr.append(li)
        row_count += 1
        if (len(li) > col_count) :
            col_count = len(li)
    except EOFError:  # EOFError 명시적으로 처리
        break

for i in range(col_count):
    for k in range(row_count):
        if k < len(arr) and i < len(arr[k]):
            print(arr[k][i], end="")

# https://www.acmicpc.net/problem/10798