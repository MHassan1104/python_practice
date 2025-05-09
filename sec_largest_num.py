# Find Second Largest: Find the second largest number in a list.
#
li=[111,111,11111,2,3,4123,123,32,4,5,4,23,5,56,6,23,65,78,9,7,123,123]
max_num=0
sec_high_num=0
for i in li:
    if i>max_num:
        sec_high_num=max_num
        max_num=i
    elif i>sec_high_num and i != max_num:
        sec_high_num=i

print(sec_high_num)
print(max_num)