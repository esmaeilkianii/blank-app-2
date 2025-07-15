"""
داشبورد اصلی برنامه
این پنجره پس از لاگین موفق نمایش داده می‌شود و شامل کارت‌های آماری،
نمودارها و دسترسی سریع به بخش‌های مختلف است.
"""
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel,
                             QGridLayout, QFrame)
from PyQt6.QtCore import Qt

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("داشبورد مدیریتی - سامانه جامع بهداری")
        self.setFixedSize(800, 600)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("font-family: Vazir; font-size: 14px;")

        # منوبار
        self.create_menu()

        # ویجت اصلی
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # عنوان
        title_label = QLabel("داشبورد اصلی")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; padding: 10px;")
        layout.addWidget(title_label)

        # گرید برای کارت‌های آماری
        stats_grid = QGridLayout()
        layout.addLayout(stats_grid)

        # افزودن کارت‌های آماری
        stats_grid.addWidget(self.create_stat_card("تعداد پرسنل", "150"), 0, 0)
        stats_grid.addWidget(self.create_stat_card("معاینات پیش‌رو", "12"), 0, 1)
        stats_grid.addWidget(self.create_stat_card("حوادث ماه جاری", "3"), 0, 2)
        stats_grid.addWidget(self.create_stat_card("تجهیزات نیازمند بررسی", "5"), 1, 0)

        # در اینجا نمودارها اضافه خواهند شد

    def create_stat_card(self, title, value):
        """
        یک کارت آماری (مانند یک QFrame) ایجاد می‌کند.
        """
        card = QFrame()
        card.setFrameShape(QFrame.Shape.StyledPanel)
        card.setLineWidth(1)
        card.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 10px;
            }
        """)

        card_layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 14px; font-weight: bold; border: none;")

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        value_label.setStyleSheet("font-size: 22px; color: #007bff; border: none;")

        card_layout.addWidget(title_label)
        card_layout.addWidget(value_label)

        card.setLayout(card_layout)
        return card

    def create_menu(self):
        """
        منوی اصلی برنامه را ایجاد می‌کند.
        """
        menu_bar = self.menuBar()
        menu_bar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        # منوی فایل
        file_menu = menu_bar.addMenu("فایل")
        exit_action = file_menu.addAction("خروج")
        exit_action.triggered.connect(self.close)

        # منوی پرسنل
        personnel_menu = menu_bar.addMenu("پرسنل")
        personnel_menu.addAction("لیست پرسنل")
        personnel_menu.addAction("افزودن پرسنل جدید")

        # منوی معاینات
        exams_menu = menu_bar.addMenu("معاینات")
        exams_menu.addAction("ثبت معاینه جدید")

        # منوی حوادث
        incidents_menu = menu_bar.addMenu("حوادث")
        incidents_menu.addAction("ثبت حادثه جدید")

        # منوی آمبولانس
        ambulance_menu = menu_bar.addMenu("آمبولانس")
        ambulance_menu.addAction("چک‌لیست روزانه")

        # منوی راهنما
        help_menu = menu_bar.addMenu("راهنما")
        help_menu.addAction("درباره نرم‌افزار")
