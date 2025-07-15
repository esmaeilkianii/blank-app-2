"""
تست واحد برای کنترلر معاینات پزشکی
"""
import unittest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base
from app.models import Personnel, MedicalExam
from app.controllers.medical_exam_controller import create_medical_exam, get_exams_for_personnel
from app.controllers.personnel_controller import create_personnel

# از یک پایگاه داده در حافظه برای تست‌ها استفاده می‌کنیم
TEST_DATABASE_URL = "sqlite:///:memory:"

class TestMedicalExamController(unittest.TestCase):

    def setUp(self):
        """
        این متد قبل از هر تست اجرا می‌شود.
        یک پایگاه داده جدید در حافظه ایجاد کرده و یک نشست (session) می‌سازد.
        """
        self.engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
        Base.metadata.create_all(self.engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = SessionLocal()

        # یک پرسنل نمونه برای استفاده در تست‌ها ایجاد می‌کنیم
        self.personnel = create_personnel(self.db, {
            "personnel_code": "test01",
            "first_name": "تست",
            "last_name": "تست زاده"
        })

    def tearDown(self):
        """
        این متد بعد از هر تست اجرا می‌شود.
        نشست را بسته و تمام جداول را از پایگاه داده حذف می‌کند.
        """
        self.db.close()
        Base.metadata.drop_all(self.engine)

    def test_create_medical_exam(self):
        """
        تست تابع create_medical_exam
        """
        exam_data = {
            "personnel_id": self.personnel.id,
            "exam_type": "ادواری",
            "exam_date": "1403/01/01",
            "result_summary": "سالم"
        }

        # ایجاد معاینه
        new_exam = create_medical_exam(self.db, exam_data)

        self.assertIsNotNone(new_exam.id)
        self.assertEqual(new_exam.exam_type, "ادواری")
        self.assertEqual(new_exam.personnel_id, self.personnel.id)

        # بررسی اینکه آیا واقعاً در دیتابیس ذخیره شده است
        retrieved_exam = self.db.query(MedicalExam).filter(MedicalExam.id == new_exam.id).first()
        self.assertIsNotNone(retrieved_exam)
        self.assertEqual(retrieved_exam.result_summary, "سالم")

    def test_get_exams_for_personnel(self):
        """
        تست تابع get_exams_for_personnel
        """
        # ایجاد دو معاینه برای پرسنل تست
        create_medical_exam(self.db, {"personnel_id": self.personnel.id, "exam_date": "1402/01/01"})
        create_medical_exam(self.db, {"personnel_id": self.personnel.id, "exam_date": "1403/01/01"})

        # دریافت معاینات
        exams = get_exams_for_personnel(self.db, self.personnel.id)

        self.assertEqual(len(exams), 2)

if __name__ == '__main__':
    unittest.main()
