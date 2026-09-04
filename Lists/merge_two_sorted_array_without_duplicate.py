arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i, j = 0, 0
n, m = len(arr1), len(arr2)
result = []
temp = float("inf")
while i < n and j < m:
    if arr1[i] >= arr2[j]:
        if temp == arr2[j]:
            j += 1
            continue
        temp = arr2[j]
        result.append(arr2[j])
        j += 1
    else:
        if temp == arr1[i]:
            i += 1
            continue
        else:
            temp = arr1[i]
            result.append(arr1[i])
            i += 1
while i < n:
    if temp == arr1[i]:
        i += 1
        continue
    temp = arr1[i]
    result.append(arr1[i])
    i += 1
while j < m:
    if temp == arr2[j]:
        j += 1
        continue
    temp = arr2[j]
    result.append(arr2[j])
    j += 1
print(result)