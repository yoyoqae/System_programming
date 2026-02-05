import sys
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QInputDialog, QMessageBox
)

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

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        create_tables()
        self.setWindowTitle("ToDo List")
        self.setGeometry(300, 200, 700, 450)

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        buttons = [
            ("Показать все задачи", self.show_tasks),
            ("Обновить задачу", self.upd_task),
            ("Добавить задачу", self.add_task),
            ("Удалить задачу", self.delete_task),
            ("Фильтр по дате", self.filter_by_date)
        ]

        for text, func in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(func)
            self.layout.addWidget(btn)

        self.setLayout(self.layout)
        self.show_tasks()

    def show_tasks(self, tasks=None):
        if tasks is None:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT List.Id, Task, Status, Categories.Name, Deadline
                FROM List
                LEFT JOIN Categories ON List.CategoryId = Categories.Id
                LEFT JOIN TaskDates ON List.Id = TaskDates.TaskId
            """)
            tasks = cursor.fetchall()
            conn.close()

        self.table.setRowCount(len(tasks))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Задача", "Статус", "Категория", "Дата"])

        for row, task in enumerate(tasks):
            for col, value in enumerate(task):
                item = QTableWidgetItem(str(value) if value is not None else "")
                self.table.setItem(row, col, item)

    def upd_task(self):
        # 1. Получаем ID
        task_id, ok = QInputDialog.getInt(self, "Обновление", "Введите ID задачи:")
        if not ok: return

        conn = connect()
        cursor = conn.cursor()

        # Проверяем существование
        cursor.execute("SELECT Task, Status FROM List WHERE Id=?", (task_id,))
        current = cursor.fetchone()

        if not current:
            QMessageBox.warning(self, "Ошибка", "Задача с таким ID не найдена")
            conn.close()
            return

        # 2. Обновляем текст задачи
        new_task, ok = QInputDialog.getText(self, "Обновление", "Новое описание:", text=current[0])
        if not ok: return

        # 3. Обновляем статус
        new_status, ok = QInputDialog.getInt(self, "Обновление", "Статус (0, 1, 2):", current[1], 0, 2)
        if not ok: return

        cursor.execute("UPDATE List SET Task=?, Status=? WHERE Id=?", (new_task, new_status, task_id))
        conn.commit()
        conn.close()
        self.show_tasks()

    def add_task(self):
        task, ok = QInputDialog.getText(self, "Задача", "Введите задачу:")
        if not ok or not task: return

        status, ok = QInputDialog.getInt(self, "Статус", "0-ожидание, 1-выполнено, 2-не выполнено", 0, 0, 2)
        if not ok: return

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT Id, Name FROM Categories")
        categories = cursor.fetchall()
        cat_text = "\n".join([f"{c[0]} - {c[1]}" for c in categories])

        cat_id, ok = QInputDialog.getInt(self, "Категория", f"Выберите ID категории:\n{cat_text}")
        if not ok:
            conn.close()
            return

        cursor.execute("INSERT INTO List (Task, Status, CategoryId) VALUES (?, ?, ?)", (task, status, cat_id))
        task_id = cursor.lastrowid

        deadline, ok = QInputDialog.getText(self, "Дата", "Введите дату (ГГГГ-ММ-ДД):")

        cursor.execute(
            "INSERT INTO TaskDates (TaskId, CreatedAt, Deadline) VALUES (?, ?, ?)",
            (task_id, datetime.now().strftime("%Y-%m-%d"), deadline if deadline else None)
        )

        conn.commit()
        conn.close()
        self.show_tasks()

    def delete_task(self):
        task_id, ok = QInputDialog.getInt(self, "Удаление", "Введите ID задачи:")
        if not ok: return

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TaskDates WHERE TaskId=?", (task_id,))
        cursor.execute("DELETE FROM List WHERE Id=?", (task_id,))
        conn.commit()
        conn.close()
        self.show_tasks()

    def filter_by_date(self):
        date, ok = QInputDialog.getText(self, "Фильтр", "Введите дату (ГГГГ-ММ-ДД):")
        if not ok or not date: return

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT List.Id, Task, Status, Categories.Name, Deadline
            FROM List
            JOIN TaskDates ON List.Id = TaskDates.TaskId
            LEFT JOIN Categories ON List.CategoryId = Categories.Id
            WHERE Deadline = ?
        """, (date,))
        tasks = cursor.fetchall()
        conn.close()

        if not tasks:
            QMessageBox.information(self, "Результат", "Задач на эту дату нет")
        else:
            self.show_tasks(tasks)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
