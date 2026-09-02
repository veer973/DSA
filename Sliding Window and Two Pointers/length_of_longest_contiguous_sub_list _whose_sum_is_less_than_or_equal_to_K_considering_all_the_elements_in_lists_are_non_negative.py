arr = list(map(int,input().split()))
k = int(input("Enter The Sum : "))
left = 0
max_length = 0
window_sum = 0
for right in range(len(arr)):
    window_sum += arr[right]
    while window_sum>k:
        window_sum -= arr[left]
        left +=1
    length = right - left +1
    if max_length<length:
        max_length = length
print(max_length)