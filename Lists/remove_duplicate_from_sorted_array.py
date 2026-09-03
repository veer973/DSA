arr = list(map(int,input().split()))
arr1 = []
dict1 = {}
for i in range(len(arr)):
    dict1[arr[i]] = 0
j = 0
for i in dict1:
    arr1.append(i)
    j+= 1

print(dict1)
print(arr1)
print("----------------------X-----------------------")
print(j)