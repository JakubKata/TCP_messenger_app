import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from ui_chat import Ui_MainWindow

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Secure E2EE Chat")

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

        self.ui.textEdit_chat.setReadOnly(True)
        self.ui.action_log_out.setEnabled(False)

        self.ui.action_close_app.triggered.connect(self.close)
        self.ui.action_log_out.triggered.connect(self.perform_logout)

        self.ui.pushButton_register.clicked.connect(self.go_to_register)
        self.ui.pushButton_back.clicked.connect(self.go_to_login)
        self.ui.pushButton_login.clicked.connect(self.perform_login)

        self.ui.listWidget_clients_list.itemClicked.connect(self.change_chat_partner)

    def go_to_register(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_register)

    def go_to_login(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

    def perform_login(self):
        


        self.ui.stackedWidget.setCurrentWidget(self.ui.page_chat)
        self.ui.action_log_out.setEnabled(True)

    def perform_logout(self):
        


        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        self.ui.action_log_out.setEnabled(False)
        self.ui.lineEdit_password.clear()
        self.ui.textEdit_chat.clear()
        self.ui.label_current_user.setText("User :")

    def change_chat_partner(self, item):
        


        selcted_user = item.text().strip()
        self.ui.label_current_user.setText(f"User : {selcted_user}")
        self.ui.textEdit_chat.clear()
        

        

    def refresh_clients_list(self):
        
        self.ui.listWidget_clients_list.clear()

        sorted_clients = sorted(
            self.users_data.items(), 
            key=lambda item: item[1]["last_active"], 
            reverse=True
        )

        for client_id, data in sorted_clients:
            status = ""
            if data["has_unread"]:
                status += "🟡 " # New message
            if data["is_online"]:
                status += "🟢 " # Online

            display_text = f"{status}{data['name']} ({client_id})"
            
            list_item = QListWidgetItem(display_text)
            
            list_item.setData(Qt.UserRole, client_id)

            self.ui.listWidget_clients_list.addItem(list_item)

    def handle_user_clicked(self, item):

        client_id = item.data(Qt.UserRole)
        
        name = self.users_data[client_id]["name"]
        self.ui.label_current_user.setText(f"User : {name} ({client_id})")
        
        self.ui.textEdit_chat.clear()

        self.users_data[client_id]["has_unread"] = False
        self.users_data[client_id]["last_active"] = time.time()

        self.refresh_clients_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec())

                     
                                        