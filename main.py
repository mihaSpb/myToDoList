from to_do_list import ToDoList


def menu():
    todo_list = ToDoList()
    actions = {
        "1": ("Добавить задачу", todo_list.add_task),
        "2": ("Отметить задачу как выполненную", todo_list.complete_task),
        "3": ("Удалить задачу", todo_list.remove_task),
        "4": ("Показать список задач", todo_list.list_tasks),
        "5": ("Выйти", None)
    }

    while True:
        print("\nМеню:")
        for key, item in actions.items():
            description = item[0]
            print(f"{key}: {description}")

        choice = input(f"\nВыберите действие: ")

        if choice == "5":
            print("Выход из программы.")
            break
        elif choice in actions:
            action = actions[choice][1]
            if action in [todo_list.add_task, todo_list.complete_task, todo_list.remove_task]:
                task = input("Введите описание задачи: ")
                action(task)
            else:
                action()
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")



if __name__ == '__main__':
    menu()