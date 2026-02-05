from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Мое первое приложение PyQt5')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        button = QPushButton('Первая кнопка')
        button2 = QPushButton('Вторая кнопка')
        button.clicked.connect(self.on_click)
        button2.clicked.connect(self.secondBtn_on_click)

        layout.addWidget(button)
        layout.addWidget(button2)

        self.setLayout(layout)

    def on_click(self):
        print(f"Кнопка первая кнопка")

    def secondBtn_on_click(self):
        print("Нажата вторая кнопка")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

#https://pythonlib.ru/library-theme97