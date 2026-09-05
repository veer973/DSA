nums = list ( map( int , input().split()))
max_profit = 0 
min_price = float("inf")
for i in range (len(nums)):
    if(min_price>nums[i]):
        min_price = nums[i]
    max_profit = max(max_profit,nums[i]-min_price)

print(max_profit)