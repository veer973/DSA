n = int(input("Enter the number: "))

original = n
digits = len(str(n))
sum = 0

while n > 0:
    temp = n % 10
    sum = sum + (temp ** digits)
    n = n // 10

if original == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")