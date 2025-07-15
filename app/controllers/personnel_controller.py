"""
کنترلر برای مدیریت پرسنل
این ماژول شامل توابع CRUD (Create, Read, Update, Delete) برای مدل پرسنل است
و منطق کسب‌وکار مربوط به اعتبارسنجی داده‌ها را پیاده‌سازی می‌کند.
"""
from sqlalchemy.orm import Session
from app.models import Personnel
from app.utils.persian_date import to_gregorian_date, to_jalali_string

def create_personnel(db: Session, personnel_data: dict) -> Personnel:
    """
    یک پرسنل جدید در پایگاه داده ایجاد می‌کند.
    """
    # اعتبارسنجی داده‌ها
    if not all([personnel_data.get("personnel_code"), personnel_data.get("first_name"), personnel_data.get("last_name")]):
        raise ValueError("کد پرسنلی، نام و نام خانوادگی الزامی است.")

    db_personnel = Personnel(
        personnel_code=personnel_data["personnel_code"],
        first_name=personnel_data["first_name"],
        last_name=personnel_data["last_name"],
        father_name=personnel_data.get("father_name"),
        national_code=personnel_data.get("national_code"),
        birth_date=personnel_data.get("birth_date"), # تاریخ شمسی به صورت رشته
        job_title=personnel_data.get("job_title"),
        employment_date=personnel_data.get("employment_date") # تاریخ شمسی به صورت رشته
    )
    db.add(db_personnel)
    db.commit()
    db.refresh(db_personnel)
    return db_personnel

def get_personnel(db: Session, personnel_id: int) -> Personnel:
    """
    اطلاعات یک پرسنل را با شناسه آن برمی‌گرداند.
    """
    return db.query(Personnel).filter(Personnel.id == personnel_id).first()

def get_all_personnel(db: Session, skip: int = 0, limit: int = 100) -> list[Personnel]:
    """
    لیست تمامی پرسنل را به صورت صفحه‌بندی شده برمی‌گرداند.
    """
    return db.query(Personnel).offset(skip).limit(limit).all()

def update_personnel(db: Session, personnel_id: int, personnel_data: dict) -> Personnel:
    """
    اطلاعات یک پرسنل را به‌روزرسانی می‌کند.
    """
    db_personnel = get_personnel(db, personnel_id)
    if not db_personnel:
        return None

    for key, value in personnel_data.items():
        setattr(db_personnel, key, value)

    db.commit()
    db.refresh(db_personnel)
    return db_personnel

def delete_personnel(db: Session, personnel_id: int) -> bool:
    """
    یک پرسنل را از پایگاه داده حذف می‌کند.
    """
    db_personnel = get_personnel(db, personnel_id)
    if not db_personnel:
        return False

    db.delete(db_personnel)
    db.commit()
    return True
