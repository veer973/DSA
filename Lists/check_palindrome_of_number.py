n = int(input("Enter the number: "))

original = n
store = n % 10
n = n // 10

while n > 0:
    temp = n % 10
    store = (store * 10) + temp
    n = n // 10

print(store)

if original == store:
    print("Number is Palindrome")
else:
    print("Number is not a Palindrome")