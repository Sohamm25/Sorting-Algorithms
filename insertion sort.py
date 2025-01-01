# 1st Solution
arr = [5, 3, 6, 1, 2, 2, 3, 6, 8, 1]
n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(arr)