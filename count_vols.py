# Count Vowels: Count the number of vowels in a string.
#
s=input("Enter string to check How many Vowels: = ")
a=0
for i in s:
    if i in "aeiou":
        a+=1
print("No. of Vowels is: = ",a)