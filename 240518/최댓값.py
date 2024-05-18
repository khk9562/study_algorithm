arr = []
max_vals = []
for _ in range(9):
    li = list(map(int, input().split()))
    arr.append(li)
    max_vals.append(max(li))

max_val = max(max_vals)
print(max_val)

for i, v in enumerate(arr):
    if max(v) == max(max_vals):
        print(f'{i+1} {arr[i].index(max(max_vals))+1}')
        
