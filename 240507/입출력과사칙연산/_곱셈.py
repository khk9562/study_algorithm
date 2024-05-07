# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# https://www.acmicpc.net/upload/images/f5NhGHVLM4Ix74DtJrwfC97KepPl27s%20(1).png
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# a, b = map(int, input("입력:").split())
# # 백의 자리
# x = b // 100
# # 십의 자리
# y = (b // 10) % 10
# # 일의 자리
# z = b % 10
# print(a*z)
# print(a*y)
# print(a*x)
# print(a*b)


# 숫자를 문자로 변환하여 슬라이싱 할 게 아니라
# 숫자의 각 자릿수를 추출해서 곱하는 식으로 해야
# ValueError 가 안나옴



a, b = map(int, input("입력:").split())
print(a*(b%10))
print(a*((b // 10) % 10))
print(a*(b // 100))
print(a*b)