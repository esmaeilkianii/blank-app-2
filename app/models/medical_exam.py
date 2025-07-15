"""
مدل داده برای معاینات پزشکی (MedicalExam)
این مدل اطلاعات مربوط به معاینات دوره‌ای و بدو استخدام پرسنل را نگهداری می‌کند.
"""
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class MedicalExam(Base):
    """
    کلاس مدل معاینات پزشکی
    """
    __tablename__ = "medical_exams"

    id = Column(Integer, primary_key=True, index=True)
    exam_type = Column(String)  # e.g., "بدو استخدام", "ادواری"
    exam_date = Column(String, nullable=False) # ذخیره تاریخ شمسی به صورت رشته
    next_exam_date = Column(String) # ذخیره تاریخ شمسی به صورت رشته
    result_summary = Column(String)

    personnel_id = Column(Integer, ForeignKey("personnel.id"))

    # تعریف رابطه
    personnel = relationship("Personnel", back_populates="medical_exams")

    def __repr__(self):
        return f"<MedicalExam(personnel_id={self.personnel_id}, date='{self.exam_date}')>"
