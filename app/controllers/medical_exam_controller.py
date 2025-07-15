"""
کنترلر برای مدیریت معاینات پزشکی
این ماژول منطق کسب‌وکار مربوط به ثبت و پیگیری معاینات را پیاده‌سازی می‌کند.
"""
from sqlalchemy.orm import Session
from app.models import MedicalExam

def create_medical_exam(db: Session, exam_data: dict) -> MedicalExam:
    """
    یک معاینه پزشکی جدید برای یک پرسنل ثبت می‌کند.
    """
    if not all([exam_data.get("personnel_id"), exam_data.get("exam_date")]):
        raise ValueError("شناسه پرسنل و تاریخ معاینه الزامی است.")

    db_exam = MedicalExam(
        personnel_id=exam_data["personnel_id"],
        exam_type=exam_data.get("exam_type"),
        exam_date=exam_data["exam_date"],
        next_exam_date=exam_data.get("next_exam_date"),
        result_summary=exam_data.get("result_summary")
    )
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def get_exams_for_personnel(db: Session, personnel_id: int) -> list[MedicalExam]:
    """
    لیست تمام معاینات یک پرسنل خاص را برمی‌گرداند.
    """
    return db.query(MedicalExam).filter(MedicalExam.personnel_id == personnel_id).all()

def get_upcoming_exams(db: Session, days_ahead: int = 30) -> list[MedicalExam]:
    """
    معایناتی که تاریخ بعدی آن‌ها در `days_ahead` روز آینده است را برمی‌گرداند.
    نکته: این تابع نیازمند تبدیل تاریخ‌های شمسی ذخیره شده به میلادی برای مقایسه است.
    پیاده‌سازی این بخش نیازمند یک منطق پیچیده‌تر است و در آینده تکمیل می‌شود.
    """
    # Placeholder: returns all exams for now
    return db.query(MedicalExam).all()
