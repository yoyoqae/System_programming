#Спроектируйте БД и напишите программу "список дел" с возможностью сохранения,
#удаления и редактирования данных. Используйте SQLite

import sqlite3
from itertools import chain


def UpdateMethod():
    conn = sqlite3.connect('ToDoList.db')
    cursor = conn.cursor()

    print("\033[33m\nСправка по статусам готовности задач\n"
                             "0 - В ожидании\n"
                             "1 - Выполнено\n"
                             "2 - Не выполнено\n\033[0m")

    cursor.execute("SELECT * FROM List")

    all_tasks = cursor.fetchall()

    print("Список ваших задач: \n", all_tasks, "\n")


    selectTaskId = int(input("\nВыберите Id задачи для ее обновления: "))

    print("0 - Назад\n"
          "1 - Обновить задачу\n"
          "2 - Обновить статус задачи\n")
    whatUpdate = int(input("\nВыберите действие: "))

    match whatUpdate:
        case 0: DisplayAllTasks()
        case 1:
            newTask = input("Введите новую задачу: ")
            cursor.execute("UPDATE List SET Task=? WHERE Id=?", (newTask, selectTaskId))
            print("Задача успешно обновлена")
        case 2:
            newStatus = input(f"Введите новый статус для задачи с Id {selectTaskId}: ")
            cursor.execute("UPDATE List SET Status=? WHERE Id=?", (newStatus, selectTaskId))
        case _:
            print("Ошибка выбора действия. Работа программы завершена")
            exit(0)

    conn.commit()
    conn.close()

def DeleteMethod():
    conn = sqlite3.connect('ToDoList.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM List")

    all_tasks = cursor.fetchall()

    print("Список ваших задач: \n", all_tasks, "\n")

    SelectForDelete = int(input("Введите Id задачи для удаления: "))

    choice = input(f"Подтвердите удаление строки:\n{cursor.execute("SELECT * FROM List WHERE Id=?"), (SelectForDelete)}\n(Да/Нет): ")

    match choice.lower():
        case "да":
            cursor.execute("DELETE FROM Task WHERE Id=?", (SelectForDelete))
        case _:
            DisplayAllTasks()

    conn.commit()
    conn.close()

def AddNewTask():
    conn = sqlite3.connect('ToDoList.db')
    cursor = conn.cursor()

    inputTask = input("Введите вашу задачу: ")

    if inputTask:
        selectStatus = int(input("Выберите статус готовности вашей задачи\n"
                             "0 - В ожидании\n"
                             "1 - Выполнено\n"
                             "2 - Не выполнено\n"
                             "Ваш выбор: "))

    while selectStatus != 0 and selectStatus != 1 and selectStatus != 2:
        print("\nОшибка выбора статуса, введите корректный статус(0-2)\n")
        selectStatus = input("Выберите статус готовности вашей задачи\n"
                             "0 - В ожидании\n"
                             "1 - Выполнено\n"
                             "2 - Не выполнено\n"
                             "Ваш выбор: ")

    executeResult = cursor.execute("INSERT INTO List (Task, Status) values(?, ?)", (inputTask, selectStatus))

    if executeResult:
        print("Задача успешно добавлена в список, статус задачи: ", selectStatus)
    else:
        print("Ошибка добавления данных!")

    DisplayAllTasks()

    conn.commit()
    conn.close()

def DisplayAllTasks():
    print("Вы находитесь на странице с вашими задачами\n")
    conn = sqlite3.connect('ToDoList.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM List")

    all_tasks = cursor.fetchall()

    print(all_tasks, "\n")

    conn.close()

    print("0 - Выход в главное меню\n"
          "1 - Добавить новую задачу\n"
          "2 - Обновить данные моих задач\n"
          "3 - Удалить задачу\n")

    choice = int(input("\nВыберите действие: "))

    match choice:
        case 0: MainMenu()
        case 1: AddNewTask()
        case 2: UpdateMethod()
        case 3: DeleteMethod()


def MainMenu():
    print("\t\t\tВы находитесь в главном меню приложения Список дел\n")

    print("0 - Выход из программы\n"
          "1 - Просмотр\редактирование моих задач\n")

    choice = int(input("Выберите действие: "))

    match choice:
        case 0:
            exit(0)
        case 1:
            DisplayAllTasks()
        case _:
            print("Ошибка выбора действия. Работа программы завершена")
            exit(0)

def IfTaskNull():
    conn = sqlite3.connect('ToDoList.db')

    cursor = conn.cursor()

    inputTask = input("Добро пожаловать в программу со списком ваших дел.\n"
                      "Введите вашу первую задачу: ")
    if inputTask:
        selectStatus = int(input("Выберите статус готовности вашей задачи\n"
                             "0 - В ожидании\n"
                             "1 - Выполнено\n"
                             "2 - Не выполнено\n"
                             "Ваш выбор: "))

    while selectStatus != 0 and selectStatus != 1 and selectStatus != 2:
        print("\nОшибка выбора статуса, введите корректный статус(0-2)\n")
        selectStatus = input("Выберите статус готовности вашей задачи\n"
                             "0 - В ожидании\n"
                             "1 - Выполнено\n"
                             "2 - Не выполнено\n"
                             "Ваш выбор: ")

    cursor.execute("INSERT INTO List (Task, Status) values(?, ?)", (inputTask, selectStatus))

    print("Задача успешно добавлена в список, статус задачи: ", selectStatus)

    conn.commit()

    conn.close()

def Table_create_Method():
    conn = sqlite3.connect('ToDoList.db')

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS List "
                   "(Id INTEGER PRIMARY KEY, "
                   "Task TEXT, "
                   "Status INTEGER DEFAULT 0)")

    cursor.execute("SELECT * FROM List")

    result = cursor.fetchall()

    conn.commit()

    conn.close()

    if not result:
        IfTaskNull()



def main():
    Table_create_Method()
    MainMenu()

main()