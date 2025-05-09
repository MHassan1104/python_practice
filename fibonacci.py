# Fibonacci Series: Generate the first n numbers in the Fibonacci sequence.

a=int(input("Enter a number for generate Fibonacci series: "))
s=0
d=1
f=0
aa=str(s)
while a>0:
    aa+= " "+str(d)
    f=d
    d=s+d
    s=f
    a-=1
print(aa)