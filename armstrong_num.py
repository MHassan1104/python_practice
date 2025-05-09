# Check Armstrong Number: Check if a number is an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153).


num=input("Enter the number : ")
sum_t=0
for i in num:
    sum_t+=int(i)**3
if sum_t==int(num):
    print("Yes this is Armstrong Number : ",num)
else:
    print("No this is Armstrong Number : ",num)
