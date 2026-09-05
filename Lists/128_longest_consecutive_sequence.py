nums = list(map(int, input().split()))

nums.sort()

if len(nums) == 0:
    print(0)
else:
    count = 1
    max_count = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] == 1:
            count += 1
        elif nums[i] == nums[i + 1]:
            continue
        else:
            count = 1

        max_count = max(count, max_count)

    print(max(count, max_count))