arr = list(map(int, input().split()))
count = 0
for right in range(len(arr)):
    left = 0
    while left < right:
        if arr[left] > arr[right]:
            count += 1
        left += 1
print(count)

'''Count inversions → one pass over all pairs is enough.
Sort the array → one pass over all pairs is not enough; you need multiple passes (or a different algorithm like Merge Sort or Quick Sort).'''