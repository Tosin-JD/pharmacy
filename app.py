import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                            QWidget, QLabel, QLineEdit, QPushButton, 
                            QListWidget, QStackedWidget, QHBoxLayout)

class PharmacyManager(QMainWindow):
    def __init__(self):
        super(PharmacyManager, self).__init__()

        self.setWindowTitle("Pharmacy Management System")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.addItem("Medicine List")
        self.sidebar.addItem("Sales")
        self.sidebar.addItem("Reports")
        self.sidebar.currentRowChanged.connect(self.change_page)
        self.sidebar.setFixedWidth(200)  # Set the width of the sidebar
        self.layout.addWidget(self.sidebar)

        # StackedWidget to manage pages
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Page 1: Medicine List
        self.page_medicine_list = QWidget()
        self.layout_medicine_list = QVBoxLayout(self.page_medicine_list)

        self.medicine_list_label = QLabel("Medicine List:")
        self.layout_medicine_list.addWidget(self.medicine_list_label)

        self.medicine_list = QListWidget()
        self.layout_medicine_list.addWidget(self.medicine_list)

        self.medicine_name_label = QLabel("Medicine Name:")
        self.layout_medicine_list.addWidget(self.medicine_name_label)

        self.medicine_name_input = QLineEdit()
        self.layout_medicine_list.addWidget(self.medicine_name_input)

        self.add_button = QPushButton("Add Medicine")
        self.add_button.clicked.connect(self.add_medicine)
        self.layout_medicine_list.addWidget(self.add_button)

        self.stacked_widget.addWidget(self.page_medicine_list)

        # Page 2: Sales
        self.page_sales = QWidget()
        self.layout_sales = QVBoxLayout(self.page_sales)
        self.layout_sales.addWidget(QLabel("Sales Page Content"))
        self.stacked_widget.addWidget(self.page_sales)

        # Page 3: Reports
        self.page_reports = QWidget()
        self.layout_reports = QVBoxLayout(self.page_reports)
        self.layout_reports.addWidget(QLabel("Reports Page Content"))
        self.stacked_widget.addWidget(self.page_reports)

        self.central_widget.setLayout(self.layout)

    def add_medicine(self):
        medicine_name = self.medicine_name_input.text()
        if medicine_name:
            self.medicine_list.addItem(medicine_name)
            self.medicine_name_input.clear()

    def change_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PharmacyManager()
    window.show()
    sys.exit(app.exec())
