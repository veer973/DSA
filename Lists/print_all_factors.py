from math import sqrt

num = int(input())
result = []
for i in range(1, int(sqrt(num))+1):
    if(num % i == 0):
        result.append(int(i))
        if(num/i !=i):
            result.append(int(num/i))
result.sort()
print(result)