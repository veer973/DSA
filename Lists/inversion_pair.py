arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    j = i + 1
    while j < len(arr):
        if arr[i] > arr[j]:
            count += 1
        j += 1
print(count)