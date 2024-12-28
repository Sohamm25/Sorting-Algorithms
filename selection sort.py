# now this is correct but not completely as i am creating a list and using min remove etc thats why we have # 2 solution
arr = [5, 3, 6, 1, 2, 2 ,3, 6, 8, 1]
arr1 = []
for i in range(len(arr)):
    a = min(arr)
    arr1.append(a)
    arr.remove(a)
print(arr1)

#2 sol
arr = [5, 3, 6, 1, 2, 2, 3, 6, 8, 1]
for i in range(len(arr)):
    Min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[Min]:
            Min = j
    arr[i], arr[Min] = arr[Min], arr[i]
print(arr)