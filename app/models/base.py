"""
ماژول پایه برای مدل‌های پایگاه داده
این ماژول شامل تنظیمات اولیه اتصال به پایگاه داده و تعریف کلاس پایه برای مدل‌ها است.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# آدرس پایگاه داده - در اینجا از یک فایل SQLite محلی استفاده می‌شود.
DATABASE_URL = "sqlite:///behdari.db"

# ایجاد موتور پایگاه داده
# `check_same_thread=False` برای استفاده در محیط‌های چندنخی مانند PyQt لازم است.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# ایجاد یک کلاس برای نشست (Session)
# این کلاس مسئول تمام ارتباطات با پایگاه داده است.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ایجاد کلاس پایه برای تمامی مدل‌ها
# تمام مدل‌های داده باید از این کلاس ارث‌بری کنند.
Base = declarative_base()

def get_db():
    """
    یک نشست پایگاه داده جدید ایجاد کرده و آن را برمی‌گرداند.
    پس از اتمام کار، نشست به طور خودکار بسته می‌شود.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Import all models here to ensure they are registered with the Base
from .user import User
from .personnel import Personnel
from .medical_exam import MedicalExam
from .incident import Incident
from .vaccination import Vaccination
from .ambulance import AmbulanceEquipment, AmbulanceChecklist

def create_database():
    """
    تمام جداول تعریف شده در مدل‌ها را در پایگاه داده ایجاد می‌کند.
    این تابع باید در اولین اجرای برنامه فراخوانی شود.
    """
    Base.metadata.create_all(bind=engine)
