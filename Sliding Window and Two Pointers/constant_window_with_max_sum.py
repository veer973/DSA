# Max. Sum With Constant Window

n = int(input("Enter The Size Of List"))
k = int(input("Enter The Window Size"))
list1 = []
for i in range(n):
    list1.append(int(input()))
left = 0
right = k
window_sum = 0
max_sum = 0
for i in range(k):
    window_sum += list1[i]
max_sum = window_sum  
while right>left and right < n:
    window_sum = window_sum + list1[right] - list1[left]
    left +=1
    right +=1
    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum) 