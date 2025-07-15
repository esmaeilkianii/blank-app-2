"""
فرم مدیریت اطلاعات پرسنل (CRUD)
این فرم برای ایجاد، مشاهده، ویرایش و حذف اطلاعات پرسنل استفاده می‌شود.
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit,
                             QPushButton, QLabel, QHBoxLayout)
from PyQt6.QtCore import Qt

class PersonnelForm(QWidget):
    def __init__(self, personnel_id=None):
        super().__init__()
        self.personnel_id = personnel_id
        self.init_ui()
        if self.personnel_id:
            self.load_personnel_data()

    def init_ui(self):
        self.setWindowTitle("فرم اطلاعات پرسنل")
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("font-family: Vazir; font-size: 12px;")

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # فیلدهای فرم
        self.personnel_code_input = QLineEdit()
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.father_name_input = QLineEdit()
        self.national_code_input = QLineEdit()
        self.birth_date_input = QLineEdit() # Later, a Jalali Calendar widget
        self.birth_date_input.setPlaceholderText("مثال: 1370/01/01")
        self.job_title_input = QLineEdit()
        self.employment_date_input = QLineEdit() # Later, a Jalali Calendar widget
        self.employment_date_input.setPlaceholderText("مثال: 1395/06/15")

        form_layout.addRow(QLabel("کد پرسنلی:"), self.personnel_code_input)
        form_layout.addRow(QLabel("نام:"), self.first_name_input)
        form_layout.addRow(QLabel("نام خانوادگی:"), self.last_name_input)
        form_layout.addRow(QLabel("نام پدر:"), self.father_name_input)
        form_layout.addRow(QLabel("کد ملی:"), self.national_code_input)
        form_layout.addRow(QLabel("تاریخ تولد:"), self.birth_date_input)
        form_layout.addRow(QLabel("سمت شغلی:"), self.job_title_input)
        form_layout.addRow(QLabel("تاریخ استخدام:"), self.employment_date_input)

        layout.addLayout(form_layout)

        # دکمه‌ها
        buttons_layout = QHBoxLayout()
        self.save_button = QPushButton("ذخیره")
        self.save_button.clicked.connect(self.save_personnel)

        self.cancel_button = QPushButton("انصراف")
        self.cancel_button.clicked.connect(self.close)

        buttons_layout.addStretch()
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.cancel_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def load_personnel_data(self):
        """
        اطلاعات پرسنل را از پایگاه داده بارگیری و در فرم نمایش می‌دهد.
        """
        # این بخش در آینده با اتصال به کنترلر تکمیل می‌شود.
        print(f"Loading data for personnel_id: {self.personnel_id}")
        # dummy data
        self.personnel_code_input.setText("12345")
        self.first_name_input.setText("علی")
        self.last_name_input.setText("رضایی")
        self.father_name_input.setText("محمد")
        self.national_code_input.setText("1234567890")
        self.birth_date_input.setText("1365/04/10")
        self.job_title_input.setText("کارشناس فنی")
        self.employment_date_input.setText("1390/01/01")


    def save_personnel(self):
        """
        اطلاعات فرم را در پایگاه داده ذخیره یا به‌روزرسانی می‌کند.
        """
        # اعتبارسنجی و ذخیره داده‌ها از طریق کنترلر انجام خواهد شد.
        print("Saving personnel data...")
        # Collect data from fields
        data = {
            "personnel_code": self.personnel_code_input.text(),
            "first_name": self.first_name_input.text(),
            "last_name": self.last_name_input.text(),
            # ... and so on for other fields
        }
        print(data)
        self.close()
