arr = list(map( int , input().split()))
size = len(arr)
result = float("inf")
arr.sort()
for i in range(size):
    if(arr[i]==i):
        continue
    else:
        result = i

if(result == float("inf")):
    print(size)
else:
    print(result)

