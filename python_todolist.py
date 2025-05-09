# Menu System Banao
# Jab program chale, user ko options do:
#
# Task dekhna
#
# Naya task add karna
#
# Task delete karna
#
# Exit karna
#
# 3. Functions Banao
# Har action ke liye ek chhoti si function likho:
#
# add_task()
#
# view_tasks()
#
# delete_task()
#
# 4. Looping System
# while True: loop use karo jo bar bar menu dikhata rahe jab tak user “exit” na kare.
#
# 5. Optional: File Save/Load (Advanced)
# Agar aap chaho to tasks ko ek file mein save kar sakte ho (todo.txt) taake program band hone ke baad bhi data na delete ho.
#
# Use open(), read(), write().

from datetime import datetime


def add_task(tasks):
    count = open('todolist.txt', 'r')
    count_line = count.readlines()
    with open("todolist.txt", "a") as f:
        f.write(str(len(count_line)+1)+" ")
        f.write(tasks)
        f.write(" ")
        f.write(datetime.today().strftime(" %m/%d/%Y, %H:%M:%S\n"))
def view_task():
    with open("todolist.txt", "r") as f:
        tasks = f.readlines()
        for i in tasks:
            print(i)

def delete_task():
    with open("todolist.txt", "r") as f:
        tasks = f.readlines()
        for i in tasks:
            print(i)
        delete = input("Which task do you want to delete? ")
        li = []
        num = 1
        for i in tasks:
            if delete == i[0]:
                print("Delete Task: ",i)
            else:
               i = i.replace(i[0], str(num))
               num = num+1
               li.append(i)
        with open("todolist.txt", "w") as fi:
            for i in li:
                fi.write(i)

def update_task():
    with open("todolist.txt", "r") as f:
        tasks = f.readlines()
        num = 1
        for i in tasks:
            print(i)
        up = input("Which task do you want to Update Task? ")
        li = []
        for i in tasks:
            if up == i[0]:
                num = i[0]
                up = input("Write task to update? Must Write task Number: ")
                li.append(num+" " + up+ datetime.today().strftime(" %m/%d/%Y, %H:%M:%S \n"))
            else:
                li.append(i)
        with open("todolist.txt", "w") as fi:
            for i in li:
                fi.write(i)



select_option = input("Enter an option which task you perform on TODO list: \nOption A For Add Task \nOption B For View Task \nOption C For Update Task \nOption D For Delete Task \nOption E For Exit\nSelect Option:  ")
while select_option != "E":
    if select_option == "A":
        task=input("Enter your task")
        add_task(task)
    elif select_option == "B":
        print("Task B")
        view_task()
    elif select_option == "C":
        update_task()
    elif select_option == "D":
        delete_task()
    select_option = input(
            "Enter an option to show TODO list: \nOption A For Add Task \nOption B For View Task \nOption C For Update Task \nOption D For Delete Task \nOption E For Exit\n Select Option: ")
