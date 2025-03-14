from to_do_list import *


def main():
    todo = ToDoList()
    todo.add_task("Сделать домашнее задание")
    todo.add_task("Написать текст")
    todo.add_task("Отправить задание на проверку")

    todo.list_tasks()

    print("\nЗадача выполнена 'Сделать домашнее задание'")
    todo.complete_task("Сделать домашнее задание")
    todo.list_tasks()

    print("\nУдаляем выполненную задачу 'Сделать домашнее задание'")
    todo.remove_task("Сделать домашнее задание")
    todo.list_tasks()

    print("\nОтмечаем несуществующую задачу 'Заказать воду':")
    todo.complete_task("Заказать воду")

    print("\nДобавляем существующую задачу 'Написать текст':")
    todo.add_task("Написать текст")
    todo.list_tasks()


main()