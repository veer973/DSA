char1 = list(input().split())
char2 = list(input().split())

hash_list = [0] * 26

for i in char1:
    ascii_value = ord(i)
    index = ascii_value - 97
    hash_list[index] += 1

for i in char2:
    ascii_value = ord(i)
    index = ascii_value - 97
    print(hash_list[index])