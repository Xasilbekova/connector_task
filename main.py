from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QMessageBox
)

from core import Core

class CreateMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Menu")
        self.setFixedSize(600,500)
        self.setStyleSheet("font-size: 35px")
        self.show()

        self.create_user = QPushButton("Create User")
        self.create_user.clicked.connect(self.showCreateUser)
        self.create_user.setStyleSheet("""
                                background-color: rgb(212, 178, 228); 
                                color: white;
                                padding: 20px;
                                margin-left: 100px;
                                margin-right: 100px;
                                border-radius: 35px;
                                font-weight: bold;
                                font-family: 'Times New Roman', Times, serif;
                                """)
        self.show_users = QPushButton("Show Users")
        self.show_users.clicked.connect(self.ShowUsersShow)
        self.show_users.setStyleSheet("""
                                background-color: rgb(212, 178, 228); 
                                color: white;
                                padding: 20px;
                                margin-left: 100px;
                                margin-right: 100px;
                                border-radius: 35px;
                                font-weight: bold;
                                font-family: 'Times New Roman', Times, serif;
                                """)
        self.update_user = QPushButton("Update User")
        self.update_user.clicked.connect(self.ShowUpdateUser)
        self.update_user.setStyleSheet("""
                                background-color: rgb(212, 178, 228); 
                                color: white;
                                padding: 20px;
                                margin-left: 100px;
                                margin-right: 100px;
                                border-radius: 35px;
                                font-family: 'Times New Roman', Times, serif;
                                font-weight: bold;
                                """)
        self.dalete_user = QPushButton("Dalete User")
        self.dalete_user.clicked.connect(self.showDaleteUser)
        self.dalete_user.setStyleSheet("""
                                background-color: rgb(212, 178, 228); 
                                color: white;
                                padding: 20px;
                                margin-left: 100px;
                                margin-right: 100px;
                                border-radius: 35px;
                                font-weight: bold;
                                font-family: 'Times New Roman', Times, serif;
                                """)

        self.vBox = QVBoxLayout()

        self.vBox.addWidget(self.create_user)        
        self.vBox.addWidget(self.show_users)        
        self.vBox.addWidget(self.update_user)        
        self.vBox.addWidget(self.dalete_user) 

        self.setLayout(self.vBox) 

    def showCreateUser(self):
        self.close()
        self.CreateUserMenu = CreateUser()
        self.CreateUserMenu.show()

    def ShowUsersShow(self):
        self.close()
        self.CreateShowMenu = ShowUsers()
        self.CreateShowMenu.show()

    def ShowUpdateUser(self):
        self.close()
        self.UpdateUser = UpdateUser()
        self.UpdateUser.show()

    def showDaleteUser(self):
        self.close()
        self.daleteUser = DaleteUser()
        self.daleteUser.show()

class CreateUser(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Create user")
        self.setFixedSize(600,500)
        self.setStyleSheet("font-size: 25px")

        self.core = Core()

        self.vBox = QVBoxLayout()

        self.fullname_edit = QLineEdit()
        self.fullname_edit.setPlaceholderText("Full name")
                
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("User name")
                
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Password")
        
        self.phone_number_edit = QLineEdit()
        self.phone_number_edit.setPlaceholderText("Mobile number")
        # self.phone_number_edit.setInputMask('+999_99_990_99_99')    buni qo'sholmadim ustoz!
        # Data too long for column 'phone_number' at row 1 error bervotti uzunligiga qo'shsamam chiqarmadi.

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_user)
        self.save_btn.clicked.connect(self.clearInput)

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.show_menu)

        self.vBox.addStretch()
        self.vBox.addWidget(self.fullname_edit)
        self.vBox.addWidget(self.username_edit)
        self.vBox.addWidget(self.password_edit)
        self.vBox.addWidget(self.phone_number_edit)
        self.vBox.addWidget(self.save_btn)
        self.vBox.addStretch()
        self.vBox.addWidget(self.menu_btn)
        self.vBox.addStretch()

        self.setLayout(self.vBox)

    def save_user(self):
        fullname = self.fullname_edit.text()
        username = self.username_edit.text()
        password = self.password_edit.text()
        phone_number = self.phone_number_edit.text()

        if fullname and username and password and phone_number:
            user = {
                'fullname': fullname,
                'username': username,
                'password': password,
                'phone_number': phone_number
            }
            self.core.insert_user(user)

    def show_menu(self):
        self.close()
        self.showMenu = CreateMenu()
        self.showMenu.show()

    def clearInput(self):
        self.fullname_edit.clear()
        self.username_edit.clear()
        self.password_edit.clear()
        self.phone_number_edit.clear()

class ShowUsers(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Show users")
        self.setFixedSize(700,500)
        self.setStyleSheet("font-size: 15px")

        self.core = Core()
        users = self.core.get_all_users()

        self.vBox = QVBoxLayout()

        self.table = QTableWidget()

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.show_menu)

        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)

        self.table.setHorizontalHeaderLabels(["id", "fullname", "username", "password", "Phone number"])
        self.table.setRowCount(len(users))

        row = 0
        for id, fullname, username, password, phone_number in users:
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row, 1, QTableWidgetItem(fullname))
            self.table.setItem(row, 2, QTableWidgetItem(username))
            self.table.setItem(row, 3, QTableWidgetItem(password))
            self.table.setItem(row, 4, QTableWidgetItem(phone_number))
            row+=1
        self.vBox.addWidget(self.table)
        self.vBox.addWidget(self.menu_btn)

        self.setLayout(self.vBox)

    def show_menu(self):
        self.close()
        self.showMenu = CreateMenu()
        self.showMenu.show()

class UpdateUser(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Update user")
        self.setFixedSize(600,500)
        self.setStyleSheet("font-size: 25px")

        self.core = Core()

        self.vBox = QVBoxLayout()
        self.info_label = QLabel()
        self.vBox.addWidget(self.info_label)

        self.id_edit = QLineEdit()
        self.id_edit.setPlaceholderText("ID")

        self.fullname_edit = QLineEdit()
        self.fullname_edit.setPlaceholderText("Full name")
        
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("User name")
        
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Password")
        
        self.phone_number_edit = QLineEdit()
        self.phone_number_edit.setPlaceholderText("Mobile number")
        # self.phone_number_edit.setInputMask('+999_99_990_99_99')         buni qo'sholmadim ustoz!

        self.save_btn = QPushButton("Update")
        self.save_btn.clicked.connect(self.change_user)

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.show_menu)

        self.vBox.addStretch()
        self.vBox.addWidget(self.id_edit)
        self.vBox.addWidget(self.fullname_edit)
        self.vBox.addWidget(self.username_edit)
        self.vBox.addWidget(self.password_edit)
        self.vBox.addWidget(self.phone_number_edit)
        self.vBox.addWidget(self.save_btn)
        self.vBox.addStretch()
        self.vBox.addWidget(self.menu_btn)
        self.vBox.addStretch()

        self.setLayout(self.vBox)

    def change_user(self):
        id = self.id_edit.text()
        fullname = self.fullname_edit.text()
        username = self.username_edit.text()
        password = self.password_edit.text()
        phone_number = self.phone_number_edit.text()

        if id and fullname and username and password and phone_number:
            user = {
                'id': id, 
                'fullname': fullname,
                'username': username,
                'password': password,
                'phone_number': phone_number
            }
        ok = self.core.update_user(user)
        self.info_label.setText(str(ok))

    def show_menu(self):
        self.close()
        self.showMenu = CreateMenu()
        self.showMenu.show()

class DaleteUser(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Dalete user")
        self.setFixedSize(600, 500)
        self.setStyleSheet("font-size: 25px")

        self.core = Core()

        self.vbox = QVBoxLayout()

        self.label = QLabel("Ma'lumotlarni o'chirish uchun ID raqam kiriting:")
        self.id_edit = QLineEdit()
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_user)

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.show_menu)

        self.vbox.addStretch()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.id_edit)
        self.vbox.addWidget(self.delete_btn)
        self.vbox.addStretch()
        self.vbox.addWidget(self.menu_btn)
        self.vbox.addStretch()

        self.setLayout(self.vbox)

    def delete_user(self):
        id = self.id_edit.text()
        if id.isdigit():
            success = self.core.delete_user(id)
            if success:
                self.id_edit.clear()
                QMessageBox.information(self, "Title", "Ma'lumot o'chirildi.")
            else:
                self.id_edit.clear()
                QMessageBox.warning(self, "Title", "Ma'lumotni o'chirib bo'lmadi.")
        else:
            self.id_edit.clear()
            QMessageBox.warning(self, "Title", "ID raqamni tekshirib qayta tekshiring.")

    def show_menu(self):
        self.close()
        self.showMenu = CreateMenu()
        self.showMenu.show()




app = QApplication([])
win = CreateMenu() 
win2 = CreateUser()
win3 = ShowUsers()
win4 = UpdateUser()
win5 = DaleteUser()
app.exec_()