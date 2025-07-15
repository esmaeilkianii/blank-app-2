"""
این پکیج شامل تمام مدل‌های داده SQLAlchemy برای پروژه است.

هر فایل یک مدل داده را تعریف می‌کند که معادل یک جدول در پایگاه داده است.
فایل base.py شامل تنظیمات اتصال و کلاس پایه برای مدل‌ها است.
"""
from .base import Base, get_db, create_database
from .user import User, UserRole
from .personnel import Personnel
from .medical_exam import MedicalExam
from .incident import Incident
from .vaccination import Vaccination
from .ambulance import AmbulanceEquipment, AmbulanceChecklist
