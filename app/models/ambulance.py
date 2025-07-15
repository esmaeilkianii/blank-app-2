"""
مدل‌های داده مربوط به آمبولانس
شامل چک‌لیست‌ها و تجهیزات آمبولانس.
"""
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class AmbulanceEquipment(Base):
    """
    کلاس مدل تجهیزات آمبولانس
    """
    __tablename__ = "ambulance_equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_consumable = Column(Boolean, default=False)
    quantity = Column(Integer, default=1)

    def __repr__(self):
        return f"<AmbulanceEquipment(name='{self.name}')>"


class AmbulanceChecklist(Base):
    """
    کلاس مدل چک‌لیست آمبولانس
    """
    __tablename__ = "ambulance_checklists"

    id = Column(Integer, primary_key=True, index=True)
    check_date = Column(String, nullable=False) # تاریخ شمسی
    shift = Column(String) # شیفت (روز/شب)
    driver_name = Column(String)
    is_complete = Column(Boolean, default=False)

    # اینجا می‌توان جزئیات چک‌لیست را به صورت یک JSON یا رابطه با جدول دیگر ذخیره کرد.
    # برای سادگی، فعلاً به همین شکل باقی می‌ماند.

    def __repr__(self):
        return f"<AmbulanceChecklist(date='{self.check_date}', shift='{self.shift}')>"
