# Remove Duplicates: Remove duplicates from a list while keeping the original order.
#
li=[3,5,4,3,6,5,3,3,2,6,7,89,9,8,7,6,6,7,8,9,8,8,8,8,9,9,0,0,0,0,0,9,98,8,7,7,6,]
ss=[]
for i in li:
    if i not in ss:
        ss.append(i)
print(ss)