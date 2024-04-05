import json

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def display_tasks(self):
        print("Todo List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {'[X]' if task['completed'] else '[ ]'} {task['task']}")

    def mark_task_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['task'] = new_task
            print("Task updated.")
        else:
            print("Invalid task index.")

    def save_and_quit(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print("Todo list saved and program exited.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. Display Todo list")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Update task")
        print("6. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_task_complete(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '6':
            filename = input("Enter filename to save todo list: ")
            todo_list.save_and_quit(filename)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
