# Mthod 1
# arr = list(map(int , input().split()))
# n = len(arr)
# dict1 = {}
# for i in range(n):
#     if arr[i] in dict1:
#         dict1[arr[i]] += 1
#     else:
#         dict1[arr[i]] = 1

# print(dict1)

# Mthod 2
arr = list(map(int , input().split()))
n = len(arr)
dict1 = {}
for i in range(n):
    dict1[arr[i]] = dict1.get(arr[i],0)+1

print(dict1)

