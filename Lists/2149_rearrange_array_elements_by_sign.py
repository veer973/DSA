nums = list(map(int , input().split()))
pos_nums = []
neg_nums =[]
result = []
for i in range(len(nums)):
    if(nums[i]>=0):
        pos_nums.append(nums[i])
    else:
        neg_nums.append(nums[i])
i , j = 0 , 0
n , m = len(pos_nums) , len(neg_nums)
while(i < n and j < m):
    result.append(pos_nums[i])
    i +=1
    result.append(neg_nums[j])
    j +=1

while(i<n):
    result.append(pos_nums[i])
    i+=1


while(j<m):
    result.append(neg_nums[j])
    j+=1

print(result)