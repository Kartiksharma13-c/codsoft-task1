class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority='Medium'):
        self.tasks.append({'task': task, 'done': False, 'priority': priority})

    def update_task(self, task_index, new_task, new_priority='Medium'):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['task'] = new_task
            self.tasks[task_index]['priority'] = new_priority
        else:
            print("Invalid task index")

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            print("Invalid task index")

    def display_tasks(self):
        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status} - Priority: {task['priority']}")
        if not self.tasks:
            print("No tasks in your list!")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Show All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            priority = input("Enter the priority (High/Medium/Low): ")
            todo_list.add_task(task, priority)
        elif choice == '2':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            new_priority = input("Enter the new priority (High/Medium/Low): ")
            todo_list.update_task(task_index, new_task, new_priority)
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
