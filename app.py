def tasks():
    tasks = [] #empty list
    print("----Welcome to the To-Do-List App----")


    total_task = int(input("Enter the no. of task you want to add :")) #6
    for i in range(1, total_task + 1): #7
        task_name = input(f"Enter the task name {i} :")
        tasks.append(task_name)

    print(f"Today's tasks are\n {tasks}")
    while True:
        operation = int(input("Enter 1 - Add\n 2 - update\n 3 - Delete\n 4 - View\n 5 - Exit/Stop/"))
        if operation == 1:
            add = input("Enter the task you want to add :")
            tasks.append(add)  
            print(f"Task {add} added successfully ....")
        
        elif operation == 2:
            updated_task = input("Enter the task you want to update :")
            if updated_task in tasks:
                up = input("Enter the new task:")
                ind = tasks.index(updated_task)
                tasks[ind] = up
                print(f"Updated task {up}")

        elif operation == 3:
            delete_task = input(f"Enter the task you want to delete:")
            if delete_task in tasks:
                ind = tasks.index(delete_task)
                del tasks[ind]
                print(f"Task {delete_task} deleted successfully ....") 
        elif operation == 4:
            print(f"Total tasks = {tasks}") 

        elif operation == 5:
            print("Thank you for using the application....")
            break
        else:
            print("Invalid Input")

print(tasks())