from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication([])
window = QWidget()
window.setWindowTitle("Пример окна")
window.setGeometry(100, 100, 400, 300)
window.show()
app.exec_()