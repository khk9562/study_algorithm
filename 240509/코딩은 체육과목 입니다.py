# 입출력이 N바이트 크기 정수라면?
# long int는 4바이트 정수까지 저장 가능
# long long int는 8바이트 정수까지 저장 가능
# int 앞에 long을 하나씩 더 붙일 때마다 4바이트씩 저장 공간이 늘어남

N = int(input())
result = ""
result += N // 4 * "long " + "int"

print(result)