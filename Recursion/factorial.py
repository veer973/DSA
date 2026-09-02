def factorial(n):
    if n ==1 or n==0 :
        result = 1
        return result
    result = n * factorial(n-1)
    return result


n = int(input("Enter the number: "))
print(factorial(n))