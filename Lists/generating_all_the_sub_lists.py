arr = list(map(int,input().split()))
for i in range(len(arr)):
    if i==0:
        print("Iteration Starts")
    else:
        print("Iteration Changes")
    print(arr[i])
    for j in range(i+1,len(arr)):
        for k in range(i,j+1):
            print(arr[k])