# Palindrome Checker: Check if a string is a palindrome (same forwards and backwards).

a=input("Enter name to check palindrome: ")
ar=""
for i in range(1,len(a)+1):
    ar+=a[-i]
if a==ar:
    print("palindrome")
else:
    print("not palindrome")