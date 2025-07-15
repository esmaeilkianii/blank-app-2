"""
فرم ثبت معاینات پزشکی
این فرم برای ثبت معاینات بدو استخدام و ادواری پرسنل استفاده می‌شود.
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit,
                             QPushButton, QLabel, QComboBox, QTextEdit)
from PyQt6.QtCore import Qt

class MedicalExamForm(QWidget):
    def __init__(self, exam_id=None, personnel_id=None):
        super().__init__()
        self.exam_id = exam_id
        self.personnel_id = personnel_id
        self.init_ui()
        if self.exam_id:
            self.load_exam_data()

    def init_ui(self):
        self.setWindowTitle("فرم ثبت معاینه پزشکی")
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("font-family: Vazir; font-size: 12px;")

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # فیلدهای فرم
        self.exam_type_combo = QComboBox()
        self.exam_type_combo.addItems(["بدو استخدام", "ادواری", "خاص"])

        self.exam_date_input = QLineEdit()
        self.exam_date_input.setPlaceholderText("مثال: 1403/05/01")

        self.next_exam_date_input = QLineEdit()
        self.next_exam_date_input.setPlaceholderText("مثال: 1404/05/01")

        self.result_summary_input = QTextEdit()

        form_layout.addRow(QLabel("نوع معاینه:"), self.exam_type_combo)
        form_layout.addRow(QLabel("تاریخ معاینه:"), self.exam_date_input)
        form_layout.addRow(QLabel("تاریخ معاینه بعدی:"), self.next_exam_date_input)
        form_layout.addRow(QLabel("خلاصه نتیجه:"), self.result_summary_input)

        layout.addLayout(form_layout)

        # دکمه‌ها
        self.save_button = QPushButton("ذخیره")
        self.save_button.clicked.connect(self.save_exam)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def load_exam_data(self):
        """
        بارگیری اطلاعات معاینه برای ویرایش.
        """
        print(f"Loading data for exam_id: {self.exam_id}")
        # Dummy data
        self.exam_type_combo.setCurrentText("ادواری")
        self.exam_date_input.setText("1402/05/01")
        self.next_exam_date_input.setText("1403/05/01")
        self.result_summary_input.setPlainText("نتیجه نرمال بود.")

    def save_exam(self):
        """
        ذخیره اطلاعات معاینه در پایگاه داده.
        """
        print("Saving medical exam data...")
        data = {
            "exam_type": self.exam_type_combo.currentText(),
            "exam_date": self.exam_date_input.text(),
            "next_exam_date": self.next_exam_date_input.text(),
            "result_summary": self.result_summary_input.toPlainText(),
            "personnel_id": self.personnel_id
        }
        print(data)
        self.close()
