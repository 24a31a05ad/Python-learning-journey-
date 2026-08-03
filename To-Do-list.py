task_list = []

def add_task():
    enter_task = input("enter a task: ")
    task_list.append(enter_task)

def rem_task():
    remove_task = input("enter a task to remove: ")
    if remove_task in task_list:
        task_list.remove(remove_task)
    else:
        print("task does not exist")

def view_task():
    print(task_list)

while True:
    print("1.add a task")
    print("2.remove a task")
    print("3.view a task")
    print("4.exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        rem_task()
    elif choice == 3:
        view_task()
    elif choice == 4:
        break
    else:
        print("invalid")