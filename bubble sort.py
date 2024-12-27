# 1 sol
arr = [5, 3, 6, 1, 2, 2 ,3, 6, 8, 1]
b = len(arr)

for i in range(b - 1):
    for j in range(i + 1, b):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

#2 sol

arr = [5, 3, 6, 1, 2, 2 ,3, 6, 8, 1]
n = len(arr)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
