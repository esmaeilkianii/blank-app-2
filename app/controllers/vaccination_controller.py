"""
کنترلر برای مدیریت واکسیناسیون
این ماژول منطق کسب‌وکار مربوط به ثبت و پیگیری واکسن‌ها و تست‌های پزشکی را پیاده‌سازی می‌کند.
"""
from sqlalchemy.orm import Session
from app.models import Vaccination

def create_vaccination(db: Session, vaccination_data: dict) -> Vaccination:
    """
    یک رکورد واکسیناسیون جدید برای یک پرسنل ثبت می‌کند.
    """
    if not all([vaccination_data.get("personnel_id"), vaccination_data.get("vaccine_name"), vaccination_data.get("vaccination_date")]):
        raise ValueError("شناسه پرسنل، نام واکسن و تاریخ تزریق الزامی است.")

    db_vaccination = Vaccination(
        personnel_id=vaccination_data["personnel_id"],
        vaccine_name=vaccination_data["vaccine_name"],
        dose_number=vaccination_data.get("dose_number"),
        vaccination_date=vaccination_data["vaccination_date"],
        next_dose_date=vaccination_data.get("next_dose_date")
    )
    db.add(db_vaccination)
    db.commit()
    db.refresh(db_vaccination)
    return db_vaccination

def get_vaccinations_for_personnel(db: Session, personnel_id: int) -> list[Vaccination]:
    """
    لیست تمام واکسن‌های یک پرسنل خاص را برمی‌گرداند.
    """
    return db.query(Vaccination).filter(Vaccination.personnel_id == personnel_id).all()
