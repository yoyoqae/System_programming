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


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDo List")
        self.setGeometry(300, 200, 700, 400)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.btn_show = QPushButton("Показать задачи")
        self.btn_add = QPushButton("Добавить задачу")
        self.btn_delete = QPushButton("Удалить задачу")
        self.btn_filter = QPushButton("Фильтр по дате")

        self.layout.addWidget(self.btn_show)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_delete)
        self.layout.addWidget(self.btn_filter)

        self.setLayout(self.layout)

        self.btn_show.clicked.connect(self.show_tasks)
        self.btn_add.clicked.connect(self.add_task)
        self.btn_delete.clicked.connect(self.delete_task)
        self.btn_filter.clicked.connect(self.filter_by_date)

        self.show_tasks()

    def show_tasks(self):
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
        self.table.setHorizontalHeaderLabels(
            ["ID", "Задача", "Статус", "Категория", "Дата"]
        )

        for row, task in enumerate(tasks):
            for col, value in enumerate(task):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def add_task(self):
        task, ok = QInputDialog.getText(self, "Задача", "Введите задачу:")
        if not ok or not task:
            return

        status, ok = QInputDialog.getInt(
            self, "Статус", "0-ожидание, 1-выполнено, 2-не выполнено", 0, 0, 2
        )
        if not ok:
            return

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT Id, Name FROM Categories")
        categories = cursor.fetchall()

        cat_text = "\n".join([f"{c[0]} - {c[1]}" for c in categories])
        cat_id, ok = QInputDialog.getInt(
            self, "Категория", f"Выберите ID категории:\n{cat_text}"
        )
        if not ok:
            conn.close()
            return

        cursor.execute(
            "INSERT INTO List (Task, Status, CategoryId) VALUES (?, ?, ?)",
            (task, status, cat_id)
        )

        task_id = cursor.lastrowid

        deadline, _ = QInputDialog.getText(
            self, "Дата", "Введите дату (ГГГГ-ММ-ДД) или оставьте пусто:"
        )

        cursor.execute(
            "INSERT INTO TaskDates (TaskId, CreatedAt, Deadline) VALUES (?, ?, ?)",
            (task_id, datetime.now().date(), deadline if deadline else None)
        )

        conn.commit()
        conn.close()

        self.show_tasks()

    def delete_task(self):
        task_id, ok = QInputDialog.getInt(
            self, "Удаление", "Введите ID задачи:"
        )
        if not ok:
            return

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM TaskDates WHERE TaskId=?", (task_id,))
        cursor.execute("DELETE FROM List WHERE Id=?", (task_id,))

        conn.commit()
        conn.close()

        self.show_tasks()

    def filter_by_date(self):
        date, ok = QInputDialog.getText(
            self, "Фильтр", "Введите дату (ГГГГ-ММ-ДД):"
        )
        if not ok or not date:
            return

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
            QMessageBox.information(self, "Результат", "Задач нет")
            return

        self.table.setRowCount(len(tasks))
        for row, task in enumerate(tasks):
            for col, value in enumerate(task):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
