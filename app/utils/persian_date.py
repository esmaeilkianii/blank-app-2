"""
ماژول ابزارهای کار با تاریخ شمسی
این ماژول توابعی برای تبدیل تاریخ میلادی به شمسی و برعکس،
و همچنین نمایش تاریخ به فرمت استاندارد فارسی فراهم می‌کند.
"""
from persiantools.jdatetime import JalaliDate
import datetime

def to_jalali_string(gregorian_date: datetime.date) -> str:
    """
    تاریخ میلادی را به رشته تاریخ شمسی تبدیل می‌کند.
    فرمت خروجی: YYYY/MM/DD
    """
    if not gregorian_date:
        return ""
    return JalaliDate(gregorian_date).strftime("%Y/%m/%d")

def to_gregorian_date(jalali_string: str) -> datetime.date:
    """
    رشته تاریخ شمسی (YYYY/MM/DD) را به تاریخ میلادی تبدیل می‌کند.
    """
    if not jalali_string:
        return None
    try:
        year, month, day = map(int, jalali_string.split('/'))
        return JalaliDate(year, month, day).to_gregorian()
    except (ValueError, TypeError):
        return None

def get_current_jalali_date() -> str:
    """
    تاریخ شمسی امروز را به صورت رشته برمی‌گرداند.
    """
    return JalaliDate.today().strftime("%Y/%m/%d")
