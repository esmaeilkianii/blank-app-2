"""
نقطه ورود اصلی برنامه سامانه جامع بهداری
این فایل مسئول اجرای برنامه، نمایش پنجره لاگین و داشبورد اصلی است.
"""
import sys
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from app.views.login import LoginWindow
from app.views.dashboard import DashboardWindow
from app.models import create_database, SessionLocal, User
from app.auth import hash_password
from app.models.user import UserRole

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = None

    def setup_database(self):
        """
        پایگاه داده و کاربر ادمین پیش‌فرض را در اولین اجرا ایجاد می‌کند.
        """
        create_database()
        db = SessionLocal()
        # اگر هیچ کاربری وجود نداشت، یک کاربر ادمین بساز
        if db.query(User).count() == 0:
            admin_user = User(
                username="admin",
                hashed_password=hash_password("admin"),
                role=UserRole.ADMIN
            )
            db.add(admin_user)
            db.commit()
            print("Admin user created successfully.")
        db.close()

    def show_splash_screen(self):
        """
        یک صفحه Splash ساده را نمایش می‌دهد.
        """
        # In a real app, you'd use a proper image
        # pixmap = QPixmap("assets/icons/splash.png")
        # splash = QSplashScreen(pixmap)
        # splash.show()
        # self.app.processEvents()
        # # Simulate loading time
        # import time
        # time.sleep(2)
        # splash.finish(self.login_window)
        pass # No splash image available yet

    def run(self):
        """
        برنامه را اجرا می‌کند.
        """
        self.setup_database()

        # پنجره لاگین را به عنوان پنجره اول نمایش بده
        self.login_window = LoginWindow(on_login_success=self.show_main_dashboard)

        self.show_splash_screen()

        self.login_window.show()
        sys.exit(self.app.exec())

    def show_main_dashboard(self):
        """
        داشبورد اصلی برنامه را نمایش می‌دهد.
        """
        self.main_window = DashboardWindow()
        self.main_window.show()

if __name__ == "__main__":
    app_instance = Application()
    app_instance.run()
