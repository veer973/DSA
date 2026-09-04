nums = list(map(int , input().split()))
count = 1
max_count  = 1
for i in range(len(arr)-1):
    if nums[i] ==1 and nums[i+1]==1 :
        count +=1
        if(count>max_count):
            max_count = count
    else:
        count =1
print(max_count)    