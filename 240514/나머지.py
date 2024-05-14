arr =[]
for i in range(10):
    arr.append(int(input()) % 42)
set_arr = set(arr)
print(len(set_arr))