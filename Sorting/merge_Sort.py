def merge_array(left_arr,right_arr):
    i,j = 0,0
    n,m = len(left_arr),len(right_arr)
    result = []
    while i <n and j<m:
        if(left_arr[i]>=right_arr[j]):
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    if(i<n):
        while(i<n):
            result.append(left_arr[i])
            i+=1
    if(j<m):
        while(j<m):
            result.append(right_arr[j])
            j+=1
    return result
def merge(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge(left_arr)
    right_arr = merge(right_arr)
    return merge_array(left_arr,right_arr)

arr = list (map (int ,input().split()))
arr = merge(arr)
print(arr)