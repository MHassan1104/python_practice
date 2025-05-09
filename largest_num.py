# Find Maximum in List: Write a function to return the largest number in a list.

def maxi(li):
    maxnum = 0
    for i in li:
        if i > maxnum:
            maxnum = i
    print("Largest num of given list: = ", maxnum)

li = [100,3,6,4,7,3,7,9,0,33,44,6,11,33,33,100]
maxi(li)