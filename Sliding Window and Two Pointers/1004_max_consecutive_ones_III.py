arr = list(map(int,input().split()))
left = 0
max_length = 0
count_for_zero =0
k = int(input())
for right in range(len(arr)):
    if arr[right] == 0:
        count_for_zero +=1
    while count_for_zero > k:
        if arr[left] == 0:
            count_for_zero -= 1
        left +=1
    length = right - left +1
    max_length = max(max_length,length)
print(max_length)        