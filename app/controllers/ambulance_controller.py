"""
کنترلر برای مدیریت آمبولانس
این ماژول منطق کسب‌وکار مربوط به چک‌لیست و تجهیزات آمبولانس را پیاده‌سازی می‌کند.
"""
from sqlalchemy.orm import Session
from app.models import AmbulanceChecklist, AmbulanceEquipment

# --- AmbulanceEquipment ---

def create_equipment(db: Session, equipment_data: dict) -> AmbulanceEquipment:
    """
    یک تجهیز جدید برای آمبولانس تعریف می‌کند.
    """
    db_equipment = AmbulanceEquipment(**equipment_data)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

def get_all_equipment(db: Session) -> list[AmbulanceEquipment]:
    """
    لیست تمام تجهیزات آمبولانس را برمی‌گرداند.
    """
    return db.query(AmbulanceEquipment).all()

# --- AmbulanceChecklist ---

def create_checklist(db: Session, checklist_data: dict) -> AmbulanceChecklist:
    """
    یک رکورد چک‌لیست جدید ثبت می‌کند.
    """
    if not all([checklist_data.get("check_date"), checklist_data.get("shift")]):
        raise ValueError("تاریخ و شیفت چک‌لیست الزامی است.")

    db_checklist = AmbulanceChecklist(
        check_date=checklist_data["check_date"],
        shift=checklist_data["shift"],
        driver_name=checklist_data.get("driver_name"),
        is_complete=checklist_data.get("is_complete", False)
        # جزئیات آیتم‌های چک شده باید به صورت جداگانه مدیریت شود
    )
    db.add(db_checklist)
    db.commit()
    db.refresh(db_checklist)
    return db_checklist

def get_all_checklists(db: Session) -> list[AmbulanceChecklist]:
    """
    تمام رکوردهای چک‌لیست را برمی‌گرداند.
    """
    return db.query(AmbulanceChecklist).order_by(AmbulanceChecklist.check_date.desc()).all()
