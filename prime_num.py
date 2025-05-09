# Prime Number Checker: Write a function to check whether a number is prime.

a=int(input("Enter a num to check Prime number or not: = "))
for i in range(2,a):
    if a%i==0:
        print("Not Prime number")
        break
else:
    print("Prime number")