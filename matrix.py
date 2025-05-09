# Matrix Transpose: Transpose a 2D matrix using nested loops.
#
row=int(input("Enter the number of Rows matrix : "))
column=int(input("Enter the number of Column matrix : "))
matrix=[]
for i in range(1,row+1):
    for j in range(1,column+1):
        print(f" {j} ",end="")
    print("")