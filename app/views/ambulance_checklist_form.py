"""
فرم چک‌لیست آمبولانس (روزانه/هفتگی)
این فرم برای ثبت وضعیت تجهیزات و آماده‌به‌کاری آمبولانس استفاده می‌شود.
"""
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit,
                             QPushButton, QLabel, QComboBox, QCheckBox, QScrollArea)
from PyQt6.QtCore import Qt

class AmbulanceChecklistForm(QWidget):
    def __init__(self, checklist_id=None):
        super().__init__()
        self.checklist_id = checklist_id
        self.init_ui()
        if self.checklist_id:
            self.load_checklist_data()

    def init_ui(self):
        self.setWindowTitle("فرم چک‌لیست آمبولانس")
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("font-family: Vazir; font-size: 12px;")
        self.setMinimumSize(500, 400)

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # فیلدهای اصلی
        self.check_date_input = QLineEdit() # Later, a Jalali Calendar
        self.check_date_input.setPlaceholderText("مثال: 1403/05/01")
        self.shift_combo = QComboBox()
        self.shift_combo.addItems(["روز", "شب"])
        self.driver_name_input = QLineEdit()

        form_layout.addRow(QLabel("تاریخ چک:"), self.check_date_input)
        form_layout.addRow(QLabel("شیفت:"), self.shift_combo)
        form_layout.addRow(QLabel("نام راننده:"), self.driver_name_input)
        main_layout.addLayout(form_layout)

        # بخش تجهیزات در یک ناحیه اسکرول‌دار
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        equipment_widget = QWidget()
        self.equipment_layout = QVBoxLayout(equipment_widget)

        # در اینجا لیست تجهیزات از پایگاه داده خوانده شده و CheckBox برای هرکدام ایجاد می‌شود
        self.add_equipment_checkbox("کپسول اکسیژن")
        self.add_equipment_checkbox("فشارسنج")
        self.add_equipment_checkbox("کیف احیا")
        self.add_equipment_checkbox("برانکارد")

        scroll_area.setWidget(equipment_widget)
        main_layout.addWidget(scroll_area)

        # دکمه‌ها
        self.save_button = QPushButton("ذخیره چک‌لیست")
        self.save_button.clicked.connect(self.save_checklist)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)

    def add_equipment_checkbox(self, equipment_name):
        """یک چک‌باکس برای تجهیزات اضافه می‌کند."""
        checkbox = QCheckBox(equipment_name)
        self.equipment_layout.addWidget(checkbox)

    def load_checklist_data(self):
        """
        بارگیری اطلاعات چک‌لیست برای مشاهده یا ویرایش.
        """
        print(f"Loading checklist data for id: {self.checklist_id}")
        # Dummy data
        self.check_date_input.setText("1403/04/20")
        self.shift_combo.setCurrentText("روز")
        self.driver_name_input.setText("احمد کریمی")
        # In a real scenario, you'd check the boxes based on saved data

    def save_checklist(self):
        """
        ذخیره اطلاعات چک‌لیست در پایگاه داده.
        """
        print("Saving ambulance checklist...")
        checked_items = []
        for i in range(self.equipment_layout.count()):
            widget = self.equipment_layout.itemAt(i).widget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                checked_items.append(widget.text())

        data = {
            "check_date": self.check_date_input.text(),
            "shift": self.shift_combo.currentText(),
            "driver_name": self.driver_name_input.text(),
            "checked_items": checked_items
        }
        print(data)
        self.close()
