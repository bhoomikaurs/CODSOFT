import json


class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description


class TaskManager:
    def __init__(self):
        self.tasks_list = []
        self.task_id_counter = 0
        self.load_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump({"task_id_counter": self.task_id_counter, "tasks_list": [
                      task.__dict__ for task in self.tasks_list]}, file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                data = json.load(file)
                self.task_id_counter = data['task_id_counter']
                self.tasks_list = [Task(**task_data)
                                   for task_data in data['tasks_list']]
        except FileNotFoundError:
            self.save_tasks()

    def display_tasks(self):
        print("*" * 5)
        if len(self.tasks_list) == 0:
            print(" Empty ")
        else:
            for index, task in enumerate(self.tasks_list, start=1):
                print(f"{index}. {task.description}")
        print("*" * 5)

    def add_task(self):
        description = input("Enter a new task: ")
        new_task = Task(self.task_id_counter + 1, description)
        self.task_id_counter += 1
        self.tasks_list.append(new_task)
        print("New task added")
        self.save_tasks()

    def edit_task(self):
        self.display_tasks()
        index = int(input("Enter the task number to edit: "))
        if 1 <= index <= len(self.tasks_list):
            new_description = input("Enter the updated task: ")
            self.tasks_list[index - 1].description = new_description
            self.save_tasks()
        else:
            print("Invalid Number")

    def delete_task(self):
        self.display_tasks()
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(self.tasks_list):
            deleted_task = self.tasks_list.pop(index - 1)
            print(f"Deleted: {deleted_task.description}")
            self.save_tasks()
        else:
            print("Invalid Number")

    def task_manager_menu(self):
        while True:
            print("\nOptions:")
            print("1. List Tasks")
            print("2. Add New")
            print("3. Edit")
            print("4. Delete")
            print("5. Exit")
            option = input("Enter the option: ")

            if option == '1':
                self.display_tasks()
            elif option == '2':
                self.add_task()
            elif option == '3':
                self.edit_task()
            elif option == '4':
                self.delete_task()
            elif option == '5':
                break
            else:
                print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    task_manager = TaskManager()
    print("Welcome")
    task_manager.task_manager_menu()
