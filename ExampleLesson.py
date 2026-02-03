import sqlite3
from datetime import datetime


DB_NAME = "ToDoList.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categories (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS List (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Task TEXT NOT NULL,
        Status INTEGER DEFAULT 0,
        CategoryId INTEGER,
        FOREIGN KEY (CategoryId) REFERENCES Categories(Id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TaskDates (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        TaskId INTEGER,
        CreatedAt TEXT,
        Deadline TEXT,
        FOREIGN KEY (TaskId) REFERENCES List(Id)
    )
    """)

    # базовые категории
    cursor.execute("INSERT OR IGNORE INTO Categories (Name) VALUES ('Учёба'), ('Работа'), ('Дом')")

    conn.commit()
    conn.close()


def show_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT List.Id, Task, Status, Categories.Name, Deadline
    FROM List
    LEFT JOIN Categories ON List.CategoryId = Categories.Id
    LEFT JOIN TaskDates ON List.Id = TaskDates.TaskId
    """)

    tasks = cursor.fetchall()

    if not tasks:
        print("Список задач пуст\n")
        return

    print("\nID | Задача | Статус | Категория | Дедлайн")
    print("-" * 60)
    for t in tasks:
        print(t)

    conn.close()


def add_task():
    conn = connect()
    cursor = conn.cursor()

    task = input("Введите задачу: ")
    if not task:
        print("Задача не может быть пустой")
        return

    status = int(input("Статус (0-ожидание, 1-выполнено, 2-не выполнено): "))

    cursor.execute("SELECT * FROM Categories")
    categories = cursor.fetchall()

    print("\nКатегории:")
    for c in categories:
        print(c)

    cat_id = int(input("Выберите ID категории: "))

    cursor.execute(
        "INSERT INTO List (Task, Status, CategoryId) VALUES (?, ?, ?)",
        (task, status, cat_id)
    )

    task_id = cursor.lastrowid
    deadline = input("Введите дедлайн (ГГГГ-ММ-ДД) или Enter: ")

    cursor.execute(
        "INSERT INTO TaskDates (TaskId, CreatedAt, Deadline) VALUES (?, ?, ?)",
        (task_id, datetime.now().date(), deadline if deadline else None)
    )

    conn.commit()
    conn.close()
    print("Задача добавлена\n")


def delete_task():
    show_tasks()
    task_id = int(input("Введите ID задачи для удаления: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM TaskDates WHERE TaskId=?", (task_id,))
    cursor.execute("DELETE FROM List WHERE Id=?", (task_id,))

    conn.commit()
    conn.close()
    print("Задача удалена\n")


def filter_by_date():
    date = input("Введите дату (ГГГГ-ММ-ДД): ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Task, Deadline
    FROM List
    JOIN TaskDates ON List.Id = TaskDates.TaskId
    WHERE Deadline = ?
    """, (date,))

    tasks = cursor.fetchall()
    print("\nЗадачи на дату", date)
    for t in tasks:
        print(t)

    conn.close()


def main_menu():
    while True:
        print("""
1 - Показать задачи
2 - Добавить задачу
3 - Удалить задачу
4 - Фильтр по дате
0 - Выход
""")
        choice = input("Выбор: ")

        match choice:
            case "1": show_tasks()
            case "2": add_task()
            case "3": delete_task()
            case "4": filter_by_date()
            case "0": break
            case _: print("Неверный ввод")


def main():
    create_tables()
    main_menu()


main()