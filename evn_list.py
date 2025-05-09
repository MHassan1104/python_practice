# List Comprehension Practice: Create a list of squares of even numbers from 1 to 20.
#
li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
r=[]
for i in range(1,21):
    if i%2==0:
        r.append(i)
print(r)