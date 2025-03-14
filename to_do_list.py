class ToDoList:
    def __init__(self):
        self.tasks = {}


    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = False
        else:
            print("Задача уже существует!")


    def complete_task (self, task):
        if task in self.tasks:
            self.tasks[task] = True
        else:
            self.task_is_null()


    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
        else:
            self.task_is_null()


    def list_tasks(self):
        print(f"\nСписок задач:")

        for task, completed in self.tasks.items():
            status = "[V]" if completed else "[X]"
            print(f"{status} {task}")


    def task_is_null(self):
        print(f"Задача отсутствует!")