# Move all zeroes to the end

nums = list(map(int, input("Enter elements: ").split()))

result = []

# Store non-zero elements
for i in range(len(nums)):
    if nums[i] != 0:
        result.append(nums[i])

# Copy them back to the original list
for i in range(len(result)):
    nums[i] = result[i]

# Fill the remaining positions with 0
for i in range(len(result), len(nums)):
    nums[i] = 0

print("Output:", nums)