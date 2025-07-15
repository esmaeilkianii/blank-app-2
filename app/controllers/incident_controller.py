"""
کنترلر برای مدیریت حوادث شغلی
این ماژول منطق کسب‌وکار مربوط به ثبت و پیگیری حوادث را پیاده‌سازی می‌کند.
"""
from sqlalchemy.orm import Session
from app.models import Incident

def create_incident(db: Session, incident_data: dict) -> Incident:
    """
    یک حادثه جدید ثبت می‌کند.
    """
    if not all([incident_data.get("personnel_id"), incident_data.get("incident_date"), incident_data.get("description")]):
        raise ValueError("شناسه پرسنل، تاریخ و شرح حادثه الزامی است.")

    db_incident = Incident(
        personnel_id=incident_data["personnel_id"],
        incident_date=incident_data["incident_date"],
        incident_time=incident_data.get("incident_time"),
        location=incident_data.get("location"),
        description=incident_data["description"],
        actions_taken=incident_data.get("actions_taken"),
        report_number=incident_data.get("report_number")
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

def get_incidents_for_personnel(db: Session, personnel_id: int) -> list[Incident]:
    """
    لیست تمام حوادث ثبت شده برای یک پرسنل را برمی‌گرداند.
    """
    return db.query(Incident).filter(Incident.personnel_id == personnel_id).all()

def get_all_incidents(db: Session) -> list[Incident]:
    """
    تمام حوادث ثبت شده را برمی‌گرداند.
    """
    return db.query(Incident).all()
