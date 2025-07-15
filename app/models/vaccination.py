"""
مدل داده برای واکسیناسیون و تست‌ها (Vaccination)
این مدل اطلاعات مربوط به واکسن‌ها و تست‌های پزشکی پرسنل را ذخیره می‌کند.
"""
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Vaccination(Base):
    """
    کلاس مدل واکسیناسیون
    """
    __tablename__ = "vaccinations"

    id = Column(Integer, primary_key=True, index=True)
    vaccine_name = Column(String, nullable=False)
    dose_number = Column(Integer)
    vaccination_date = Column(String, nullable=False) # ذخیره تاریخ شمسی
    next_dose_date = Column(String) # ذخیره تاریخ شمسی

    personnel_id = Column(Integer, ForeignKey("personnel.id"))

    # تعریف رابطه
    personnel = relationship("Personnel", back_populates="vaccinations")

    def __repr__(self):
        return f"<Vaccination(personnel_id={self.personnel_id}, vaccine='{self.vaccine_name}')>"
