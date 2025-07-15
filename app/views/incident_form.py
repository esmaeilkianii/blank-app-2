"""
فرم ثبت حادثه شغلی
این فرم برای ثبت و پیگیری حوادث مطابق با استانداردهای HSE استفاده می‌شود.
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit,
                             QPushButton, QLabel, QTextEdit, QTimeEdit)
from PyQt6.QtCore import Qt, QTime

class IncidentForm(QWidget):
    def __init__(self, incident_id=None, personnel_id=None):
        super().__init__()
        self.incident_id = incident_id
        self.personnel_id = personnel_id
        self.init_ui()
        if self.incident_id:
            self.load_incident_data()

    def init_ui(self):
        self.setWindowTitle("فرم ثبت حادثه")
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("font-family: Vazir; font-size: 12px;")

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # فیلدهای فرم
        self.report_number_input = QLineEdit()
        self.incident_date_input = QLineEdit()
        self.incident_date_input.setPlaceholderText("مثال: 1403/05/01")
        self.incident_time_input = QTimeEdit()
        self.incident_time_input.setDisplayFormat("hh:mm")
        self.location_input = QLineEdit()
        self.description_input = QTextEdit()
        self.actions_taken_input = QTextEdit()

        form_layout.addRow(QLabel("شماره گزارش:"), self.report_number_input)
        form_layout.addRow(QLabel("تاریخ حادثه:"), self.incident_date_input)
        form_layout.addRow(QLabel("ساعت حادثه:"), self.incident_time_input)
        form_layout.addRow(QLabel("محل حادثه:"), self.location_input)
        form_layout.addRow(QLabel("شرح حادثه:"), self.description_input)
        form_layout.addRow(QLabel("اقدامات انجام شده:"), self.actions_taken_input)

        layout.addLayout(form_layout)

        # دکمه‌ها
        self.save_button = QPushButton("ذخیره")
        self.save_button.clicked.connect(self.save_incident)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def load_incident_data(self):
        """
        بارگیری اطلاعات حادثه برای ویرایش.
        """
        print(f"Loading data for incident_id: {self.incident_id}")
        self.report_number_input.setText("INC-001")
        self.incident_date_input.setText("1403/02/15")
        self.incident_time_input.setTime(QTime(10, 30))
        self.location_input.setText("خط تولید ۲")
        self.description_input.setPlainText("لغزش و افتادن از پله.")
        self.actions_taken_input.setPlainText("کمک‌های اولیه انجام شد و به بیمارستان منتقل شد.")


    def save_incident(self):
        """
        ذخیره اطلاعات حادثه در پایگاه داده.
        """
        print("Saving incident data...")
        data = {
            "report_number": self.report_number_input.text(),
            "incident_date": self.incident_date_input.text(),
            "incident_time": self.incident_time_input.text(),
            "location": self.location_input.text(),
            "description": self.description_input.toPlainText(),
            "actions_taken": self.actions_taken_input.toPlainText(),
            "personnel_id": self.personnel_id
        }
        print(data)
        self.close()
