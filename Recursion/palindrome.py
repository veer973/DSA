def pallindroome(str1,left,right):
    result = True
    if left>=right:
        result = True
        return result
    else:
        if(str1[left]==str1[right]):
            result =True
        else:
            result = False
            return result
        return pallindroome(str1,left+1,right-1)

str1 = input("Enter the string : ")
if not (pallindroome(str1,0,len(str1)-1)):
   print("Not A Palindrome")
else:
    print("It is a Palindrome") 