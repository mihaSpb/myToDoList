class ToDoList:
    def __init__(self):
        self.tasks = {}


    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = False
            print(f"Задача '{task}' добавлена.")
        else:
            print(f"Задача '{task}' уже существует!")


    def complete_task (self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f"\nЗадача '{task}' отмечена как выполненная.")
        else:
            self.task_is_null(task)


    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"\nЗадача '{task}' удалена.")
        else:
            self.task_is_null(task)


    def list_tasks(self):
        if not self.tasks:
            print(f"\nСписок задач пуст")
        else:
            for task, completed in self.tasks.items():
                status = "[V]" if completed else "[X]"
                print(f"{status} {task}")


    def task_is_null(self, task):
        print(f"Задачи '{task}' не существует!")
