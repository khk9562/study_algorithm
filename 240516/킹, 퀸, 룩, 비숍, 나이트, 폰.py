arr =[1, 1, 2, 2, 2, 8]
킹, 퀸, 룩, 비숍, 나이트, 폰 = map(int, input().split())
print(arr[0]-킹, end=" ")
print(arr[1]-퀸, end=" ")
print(arr[2]-룩, end=" ")
print(arr[3]-비숍, end=" ")
print(arr[4]-나이트, end=" ")
print(arr[5]-폰)
# print(arr[0]-킹, arr[1]-퀸, arr[2]-룩, arr[3]-비숍, arr[4]-나이트, arr[5]-폰)