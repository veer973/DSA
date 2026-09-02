arr = list(map(int,input().split()))
arr1 = arr.copy()
arr1.reverse()
n = len(arr)
k = int(input("Enter The Number Of Cards: "))
left_sum = 0
right_sum =0
right_reverse_index = 0
max_sum=0
right_sum1 = 0
for i in range(k):
    left_sum += arr[i]
for i in range(k):
    right_sum += arr1[i]
if left_sum>right_sum:
    max_sum = left_sum
else:
    max_sum=right_sum
for i in range(k-1,-1,-1):
    left_sum -= arr[i]
    right_sum1 += arr1[right_reverse_index]
    right_reverse_index += 1
    sum = left_sum + right_sum1
    if sum>max_sum:
        max_sum = sum

print(max_sum)