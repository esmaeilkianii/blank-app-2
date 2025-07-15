"""
پنجره لاگین
این پنجره از کاربر نام کاربری و رمز عبور را دریافت کرده و پس از اعتبارسنجی،
او را به داشبورد اصلی هدایت می‌کند.
"""
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QLabel, QMessageBox)
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ورود به سامانه جامع بهداری")
        self.setFixedSize(350, 200)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        layout = QVBoxLayout()

        # فونت و استایل
        self.setStyleSheet("font-family: Vazir; font-size: 12px;")

        self.username_label = QLabel("نام کاربری:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("نام کاربری خود را وارد کنید")

        self.password_label = QLabel("رمز عبور:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("رمز عبور خود را وارد کنید")

        self.login_button = QPushButton("ورود")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        """
        عملیات لاگین را با استفاده از کنترلر مربوطه انجام می‌دهد.
        """
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "خطا", "نام کاربری و رمز عبور نمی‌توانند خالی باشند.")
            return

        from app.auth import login
        from app.models import SessionLocal

        db = SessionLocal()
        try:
            if login(db, username, password):
                self.on_login_success()
                self.close()
            else:
                QMessageBox.critical(self, "خطا", "نام کاربری یا رمز عبور اشتباه است.")
        finally:
            db.close()


if __name__ == '__main__':
    # این بخش برای تست مستقل این پنجره است
    app = QApplication(sys.argv)

    def on_success():
        print("Login successful, opening main dashboard...")

    login_win = LoginWindow(on_login_success=on_success)
    login_win.show()
    sys.exit(app.exec())
