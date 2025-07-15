"""
مدل داده برای پرسنل (Personnel)
این مدل اطلاعات فردی و شغلی هر یک از کارکنان را ذخیره می‌کند.
"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base

class Personnel(Base):
    """
    کلاس مدل پرسنل
    """
    __tablename__ = "personnel"

    id = Column(Integer, primary_key=True, index=True)
    personnel_code = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    father_name = Column(String)
    national_code = Column(String, unique=True)
    birth_date = Column(String) # ذخیره تاریخ شمسی به صورت رشته
    job_title = Column(String)
    employment_date = Column(String) # ذخیره تاریخ شمسی به صورت رشته

    # تعریف روابط
    medical_exams = relationship("MedicalExam", back_populates="personnel")
    incidents = relationship("Incident", back_populates="personnel")
    vaccinations = relationship("Vaccination", back_populates="personnel")

    def __repr__(self):
        return f"<Personnel(full_name='{self.first_name} {self.last_name}', code='{self.personnel_code}')>"
