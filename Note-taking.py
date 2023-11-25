import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox


class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QListWidget()
        self.task_list.itemClicked.connect(self.task_completed)
        self.task_list.setSortingEnabled(True)

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)

        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            self.tasks.append(task_text)
            self.task_list.addItem(task_text)
            self.task_input.clear()

    def task_completed(self, item):
        completed_task = item.text()
        QMessageBox.information(self, "Task Completed", f"Completed: {completed_task}")
        self.tasks.remove(completed_task)
        self.task_list.takeItem(self.task_list.row(item))

    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            task = item.text()
            self.tasks.remove(task)
            self.task_list.takeItem(self.task_list.row(item))

    def show(self):
        super().show()


def main():
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
