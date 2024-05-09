while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
# 그냥 break 없이 무한 루프 돌리면 런타임 에러 남
# 에러가 안날때까지 루프 돌리기