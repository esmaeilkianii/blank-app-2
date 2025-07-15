"""
فرم مدیریت واکسیناسیون و تست‌ها
این فرم برای ثبت اطلاعات واکسن‌ها و تست‌های پزشکی پرسنل استفاده می‌شود.
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit,
                             QPushButton, QLabel, QSpinBox)
from PyQt6.QtCore import Qt

class VaccinationForm(QWidget):
    def __init__(self, vaccination_id=None, personnel_id=None):
        super().__init__()
        self.vaccination_id = vaccination_id
        self.personnel_id = personnel_id
        self.init_ui()
        if self.vaccination_id:
            self.load_vaccination_data()

    def init_ui(self):
        self.setWindowTitle("فرم ثبت واکسیناسیون")
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("font-family: Vazir; font-size: 12px;")

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # فیلدهای فرم
        self.vaccine_name_input = QLineEdit()
        self.dose_number_input = QSpinBox()
        self.dose_number_input.setMinimum(1)
        self.vaccination_date_input = QLineEdit()
        self.vaccination_date_input.setPlaceholderText("مثال: 1403/05/01")
        self.next_dose_date_input = QLineEdit()
        self.next_dose_date_input.setPlaceholderText("مثال: 1404/05/01 (اختیاری)")

        form_layout.addRow(QLabel("نام واکسن/تست:"), self.vaccine_name_input)
        form_layout.addRow(QLabel("نوبت (دوز):"), self.dose_number_input)
        form_layout.addRow(QLabel("تاریخ تزریق/انجام:"), self.vaccination_date_input)
        form_layout.addRow(QLabel("تاریخ نوبت بعدی:"), self.next_dose_date_input)

        layout.addLayout(form_layout)

        # دکمه‌ها
        self.save_button = QPushButton("ذخیره")
        self.save_button.clicked.connect(self.save_vaccination)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def load_vaccination_data(self):
        """
        بارگیری اطلاعات واکسن برای ویرایش.
        """
        print(f"Loading data for vaccination_id: {self.vaccination_id}")
        self.vaccine_name_input.setText("کزاز")
        self.dose_number_input.setValue(2)
        self.vaccination_date_input.setText("1400/10/10")
        self.next_dose_date_input.setText("1410/10/10")

    def save_vaccination(self):
        """
        ذخیره اطلاعات واکسن در پایگاه داده.
        """
        print("Saving vaccination data...")
        data = {
            "vaccine_name": self.vaccine_name_input.text(),
            "dose_number": self.dose_number_input.value(),
            "vaccination_date": self.vaccination_date_input.text(),
            "next_dose_date": self.next_dose_date_input.text(),
            "personnel_id": self.personnel_id
        }
        print(data)
        self.close()
