# Number of Words: Count how many words are in a given sentence.

s=input("Enter Sentance to check How many words : = ")
n=0
a=s.split(" ")
for i in a:
    for x in i:
        n += 1
print("No. of words is: = ",n)
