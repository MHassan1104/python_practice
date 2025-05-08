# Practice day 01
# memory management in python
# Data Structures in Python, also see there difference, and also about there complexity, which one is fastest and why
# types of loops, and also there execution with different data structures
from random import randint


#add 7 fruit in list by enter user

# li=[]
# li.append(input("Enter 7 Fruit name"))
# li.append(input("<UNK>"))
# li.append(input("<UNK>"))
# li.append(input("<UNK>"))
# li.append(input("<UNK>"))
# li.append(input("<UNK>"))
# li.append(input("<UNK>"))
#
# print(li)

# num=[]
# num.append(int(input("Enter student num \nMath")))
# num.append(int(input("Physics")))
# num.append(int(input("Chemistry")))
# num.append(int(input("Biology")))
# num.append(int(input("English")))
# num.sort()
# print(num)

# dic={"tera":"your","mera":"My","hamara":"our","pyaar":"love"}
# print(dic.values())
# nam=input("if you want to meaning of word enter word \n")
# print(dic[nam])

# s=set()
# s.add(int(input("Enter num 1: ")))
# s.add(int(input("Enter num 2: ")))
# s.add(int(input("Enter num 3: ")))
# s.add(int(input("Enter num 4: ")))
# s.add(int(input("Enter num 5: ")))
# s.add(int(input("Enter num 6: ")))
# s.add(int(input("Enter num 7: ")))
# s.add(int(input("Enter num 8: ")))
# print(s)

# s={18,"18"}
# print(type(s),s)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))

# dic={}
# print(type(dic))

# dic={}
# name=input("Enter your name: ")
# lan=input("Enter your language: ")
# name1=input("Enter your name: ")
# lan1=input("Enter your language: ")
# name2=input("Enter your name: ")
# lan2=input("Enter your language: ")
# name3=input("Enter your name: ")
# lan3=input("Enter your language: ")
# dic.update({ name: lan})
# dic.update({ name1: lan1})
# dic.update({ name2: lan2})
# dic.update({ name3: lan3})
# print(dic)

# num=int(input("Enter a number 1: "))
# num1=int(input("Enter a number 2: "))
# num2=int(input("Enter a number 3: "))
# num3=int(input("Enter a number 4: "))
# if num>num1 and num>num2 and num>num3:
#     print(num)
# elif num1>num and num1>num2 and num1>num3:
#     print(num1)
# elif num2>num and num2>num1 and num2>num3:
#     print(num2)
# elif num3>num and num3>num1 and num3>num2 :
#     print(num3)
# else:
#     print("every numbers are equal")


# n1=int(input("Enter the first Subject Marks: "))
# n2=int(input("Enter the second Subject Marks: "))
# n3=int(input("Enter the third Subject Marks: "))
#
# p=(100*(n1+n2+n3))/300
# if p>=40 and n1>33 and n2>33 and n3>33:
#     print("Hurry You are passed")
# else:
#     print("Failed Try again next Year")

# p1="make alot of money"
# p2="click this"
# p3="buy now"
# p4="subscribe this"
#
# commm=input("enter your comment")
#
# if p1 in commm or p2 in commm or p3 in commm or p4 in commm:
#     print("This is spam message")
# else:
#     print("This is not a spam message")

# user=input("enter your name")
# if len(user)<10:
#     print("yes this name contains less then 10 characters")
# else:
#     print("this name contain greater then 10 characters")

# li={"Hassan","hannan","zahid","ali","usama","usman"}
# nam=input("Enter your name:")
# if nam in li:
#     print("Hurry yes you are invited")
# else:
#     print("Sorry you are not invited because your name is not in the list")
#

# marks=int(input("Enter marks: "))
# if marks >= 90:
#     print("Ex")
# elif (marks >= 80 and marks < 90):
#     print("A")
# elif (marks >= 70 and marks < 80):
#     print("B")
# elif (marks >= 60 and marks < 70):
#     print("C")
# elif marks >= 50 and marks < 60:
#     print("D")
# elif marks<50:
#     print("Fail")
# print("Your grade is",marks)

# post=input("Enter your post: ")
# if "Herry".lower() in post.lower():
#     print("Yes This post is about Herry")
# else:
#     print("Post is not about Herry")


# table=int(input("Enter the table number: "))
# for i in range(10):
#     i+=1
#     print(f"{table} * {i} = ",table*i)


# s=["Hassan","Hannan","Zahid","Usama"]
#
# for i in s:
#     print(f"Hello {i}, How are you? ")

# table=int(input("Enter the table number: "))
# i=1
# while i<=10:
#     print(f"{table} * {i} = ",table*i)
#     i+=1


# n=int(input("Enter a number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# n=int(input("Enter a number: "))
# i=1
# sum=0
# print(type(sum))
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("The sum is",sum)


# n=int(input("Enter a number: "))
# i=n
# sum=1
# while(i>=1):
#     sum=sum*i
#     i-=1
# print("Factorial is = ",sum)


# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print("*"* (i))

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "* (n-i),end="")
#     print("*"* i)



# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n,end="")
#         print("")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*")

# n=int(input("Enter a number: "))
# i=n
# for i in range(1,11):
#     print(f"{n} * {11-i} = {n * (11-i)}")

# def greater(a,b,c):
#     if a > b and a > c:
#         print(f"{a} is greater than {b} and {c} ")
#     elif b > a and b > c:
#         print(f"{b} is greater than {a} and {c} ")
#     else:
#         print(f"{c} is greater than {b} and {a} ")
#
#
# greater(int(input("num1")),int(input("num2")),int(input("num3")))


# def celcius(f):
#     c=5*(f-32)/9
#
#     return c
#
# s=celcius(int(input("Enter the temperature in Celcius: ")))
# print("The temperature in Celcius is: ",s," degrees Celcius")


# def sumf(n):
#     if n == 0:
#         return 0
#     return n + sumf(n-1)
#
# print(sumf(int(input("Enter a number for sum: "))))


# def star(n):
#     if n==0:
#         return
#     print('*'* n)
#     star(n-1)
#
# star(3)



# def inctocm(n):
#     return n *2.54
# print(inctocm(float(input('Enter a inches to covert centimeter: '))))


# def rem(s,word):
#     n=[]
#     for c in s:
#         if not(c==word):
#             n.append(c.strip(word))
#     return n
#
# li=["hassan","ali","usama","usman","zahid","hannan"]

# print(rem(li,"an"))


# def table(n,i=1):
#     if i==11:
#         return
#     print(f"{n} * {i} = {n * i}")
#     table(n,i+1)
# table(5)

# f=open("file.txt")
# f.write("hello world")
# f.write("Hello World323")
# l=f.readlines()
# for line in l:
#     print(line)
# a=f.readline()
# a2=f.readline()
# a3=f.readline()
# a4=f.readline()
# print(a,a2,a3,a4)

# with open("poems.txt") as f:
#     if ("Twinkle" in f.read()):
#         print("Find this poem")
#     else:
#         print("No poem")


# import random
# def game():
#     sc = random.randint(1, 100)
#     print(sc)
#     with open("hiscore.txt") as f:
#         a=f.read()
#         if a!="":
#             a=int(a)
#         else:
#             a=0
#         if int(a)<sc:
#             with open("hiscore.txt","w") as s:
#                 s.write(str(sc))
#                 print("add greater")
#         else:
#             print("nothing")
# game()


# def genrat(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{n} * {i}= {n*i} \n"
#         with open(f"tables/table{n}.txt","w") as f:
#             f.write(table)
#
# for i in range(2,20):
#     genrat(i)


# word="monkey"
# with open("file.txt")as f:
#     content=f.read()
# content=content.replace(word,"######")
#
# with open("file.txt","w") as f:
#     f.write(content)

# words=["monkey","donkey","ganda"]
# with open("file.txt","r") as f:
#     content=f.read()
#     for word in words:
#         content=content.replace(word,"#"*len(word))
# with open("file.txt","w") as f:
#     f.write(content)


# with open("file.txt") as f:
#     i=0
#     a=1
#     content=f.readlines()
#     for line in content:
#         if("python" in line):
#             print(f"Yes we find Python Line number is {a}")
#             i=1
#         a = a + 1
#     if(i==0):
#         print("No python found")
#

# with open("file.txt") as file:
#     content=file.read()
# with open("file_copy.txt","w") as file:
#     file.write(content)


# with open("file.txt") as file:
#     content=file.read()
# with open("file_copy.txt") as file:
#     content2=file.read()
# if content==content2:
#     print("Contents are equal")
# else:
#     print("Contents are not equal")


# class Programmer(object):
#     def __init__(self, name, age, company,pin,post):
#         self.name = name
#         self.age = age
#         self.company=company
#         self.pin = pin
#         self.post = post
#
# p=Programmer("Hassan",25,"Microsoft",2312,"Software Engineer")
# print(p.name)
# print(p.age)
# print(p.company)
# print(p.pin)
# print(p.post)


# class Calculator:
#     def __init__(self, num1):
#         self.num1 = num1
#     def square(self):
#         return self.num1 * self.num1
#     def cube(self):
#         return self.num1 ** 3
#     def squareRoot(self):
#         return self.num1 ** 0.5
# c=Calculator(4)
# print(c.square())
# print(c.cube())
# print(c.squareRoot())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @staticmethod
#     def greeting():
#         print("Good Morning")
# p=Person("John", 36)
# p.greeting()

# class Train:
#     seat=0
#     fair=5000
#     remainingseat=20
#     def bookticket(self):
#         self.seat=int(input("How many seats you Booked ticket"))
#
#     def getstatus(self):
#         if self.seat>=1:
#             print("Congrats Your Seats are booked")
#         else:
#             print(f"Sorry Your Seats are not booked \nPlease Book your seat and remaining seats {self.remainingseat-self.seat}")
#     def getfairr(hassan):
#         if hassan.seat>=1:
#             return f"Your total Fair is: {hassan.fair * hassan.seat} \nRemaining seats are: {hassan.remainingseat - hassan.seat}"
#         return ""
#
#
# t=Train()
# t.bookticket()
# t.getstatus()
# print(t.getfairr())

# class Train:
#     def __init__(self, trainno):
#         self.trainno = trainno
#     def book(self, fro,to):
#         print(f"Ticket is booked is {self.trainno} from {fro} is {to}")
#     def getstatus(self):
#         print(f"Train no {self.trainno} is running on time")
#     def getfare(self):
#         print(f"Train Fare is train no {self.trainno} is {randint(1500,10000)}")
#
# t=Train(125120)
# t.book("ISL","LHR")
# t.getstatus()
# t.getfare()


class TwoDvector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def show(self):
        print(f"{self.a}i, {self.b}j = {0}")

class ThreeDvector(TwoDvector):
    def __init__(self, c):
        super.__init__(self, a)
        self.c = c
