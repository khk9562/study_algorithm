N = int(input())
# 전체 길이 N이고, 오른쪽 정렬
for i in range(1, N+1):
    print(" "*(N-i) + "*"*i)
    # 이렇게하면 
    # TypeError: unsupported operand type(s) for -: 'str' and 'int'
    # print((" "*N+1-i+"*"*i))