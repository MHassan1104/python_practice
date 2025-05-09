# Factorial Calculator: Write a function to compute the factorial of a number.


b=int(input("Enter a number to find Factorial: = "))
s=1
while b > 0:
    s*=b
    b-=1
print("Factorial is = ",s)
