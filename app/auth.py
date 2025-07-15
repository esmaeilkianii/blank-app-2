"""
ماژول احراز هویت و مدیریت دسترسی
این ماژول شامل توابع مربوط به:
- هش کردن و بررسی رمزهای عبور با استفاده از bcrypt.
- مدیریت نشست (session) کاربر فعلی.
- کنترل دسترسی مبتنی بر نقش (Role-Based Access Control).
"""
import bcrypt
from .models import User, UserRole

# متغیری برای نگهداری کاربر لاگین کرده فعلی
# این یک راه ساده برای مدیریت نشست است. در برنامه‌های بزرگ‌تر می‌توان از روش‌های پیچیده‌تری استفاده کرد.
current_user = None

def hash_password(password: str) -> bytes:
    """
    رمز عبور را با استفاده از bcrypt هش می‌کند.
    """
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt)

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """
    رمز عبور وارد شده را با رمز عبور هش‌شده مقایسه می‌کند.
    """
    password_bytes = plain_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)

def login(db_session, username, password) -> bool:
    """
    کاربر را با نام کاربری و رمز عبور احراز هویت می‌کند.
    اگر موفقیت‌آمیز بود، کاربر را در current_user ذخیره کرده و True برمی‌گرداند.
    """
    global current_user
    user = db_session.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        current_user = user
        return True
    return False

def logout():
    """
    کاربر فعلی را از نشست خارج می‌کند.
    """
    global current_user
    current_user = None

def get_current_user() -> User:
    """
    کاربر لاگین کرده فعلی را برمی‌گرداند.
    """
    return current_user

def role_required(roles: list[UserRole]):
    """
    یک دکوراتور برای محدود کردن دسترسی به یک تابع بر اساس نقش کاربر.
    مثال:
    @role_required([UserRole.ADMIN, UserRole.MANAGER])
    def my_admin_function():
        ...
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not current_user or current_user.role not in roles:
                # در یک برنامه واقعی، اینجا یک Exception یا پیام خطا نمایش داده می‌شود.
                print(f"Access Denied: Required roles {roles}")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator
