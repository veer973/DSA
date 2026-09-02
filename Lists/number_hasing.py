# Hash list works efficiently when the input values have a fixed/small range.
# For an unknown or large range of values, use a dictionary.

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

hash_list = [0] * 11

for i in arr1:
    hash_list[i] += 1

for i in arr2:
    if i < 0 or i > 10:
        print(0)
    else:
        print(hash_list[i])


