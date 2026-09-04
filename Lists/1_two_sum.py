nums = list(map(int, input("Enter the element of array: ").split()))

target = int(input("Enter the target: "))

dict1 = {}

for i in range(len(nums)):

    need = target - nums[i]

    if need in dict1:
        print(i)
        print(dict1[need])

    dict1[nums[i]] = i