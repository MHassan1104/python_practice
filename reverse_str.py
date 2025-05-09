# Reverse a String: Reverse a given string without using slicing.

s=input("enter string: = ")
ar=""
for i in range(1,len(s)+1):
    ar+=s[-i]
print(ar)