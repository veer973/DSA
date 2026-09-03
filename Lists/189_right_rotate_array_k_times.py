def rotate1time(arr,k):
    if(k == 0):
        return arr
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return rotate1time(arr, k-1)

arr = list (map( int ,input("Enter the elements of array : ").split()))
k = int(input("Enter how many times you wanted to rotate: "))
print(rotate1time(arr,k))


