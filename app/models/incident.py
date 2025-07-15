"""
مدل داده برای حوادث شغلی (Incident)
این مدل برای ثبت و پیگیری حوادث مطابق با استانداردهای HSE استفاده می‌شود.
"""
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Incident(Base):
    """
    کلاس مدل حوادث
    """
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_date = Column(String, nullable=False) # ذخیره تاریخ شمسی
    incident_time = Column(String) # ذخیره زمان
    location = Column(String)
    description = Column(String, nullable=False)
    actions_taken = Column(String)
    report_number = Column(String, unique=True)

    personnel_id = Column(Integer, ForeignKey("personnel.id"))

    # تعریف رابطه
    personnel = relationship("Personnel", back_populates="incidents")

    def __repr__(self):
        return f"<Incident(report_number='{self.report_number}', date='{self.incident_date}')>"
