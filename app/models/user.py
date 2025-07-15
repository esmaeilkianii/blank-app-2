"""
مدل داده برای کاربران سیستم (User)
این مدل اطلاعات مربوط به کاربران، شامل نام کاربری، رمز عبور هش‌شده و نقش آن‌ها را ذخیره می‌کند.
"""
from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from .base import Base
import enum

class UserRole(enum.Enum):
    """
    نقش‌های مختلف کاربران در سیستم
    - Admin: دسترسی کامل به تمام بخش‌ها
    - Manager: مدیر (دسترسی به داشبورد و گزارش‌ها)
    - Doctor: پزشک
    - Nurse: پرستار
    - HSE: کارشناس HSE
    """
    ADMIN = "admin"
    MANAGER = "manager"
    DOCTOR = "doctor"
    NURSE = "nurse"
    HSE = "hse"

class User(Base):
    """
    کلاس مدل کاربر
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role.value}')>"
