def reverse(arr,left,right):
    if left>=right:
        return arr
    arr[left],arr[right] = arr[right],arr[left]
    reverse(arr,left+1,right-1)

arr = list (map (int ,input().split()))
reverse(arr,0,len(arr)-1)
print(arr)