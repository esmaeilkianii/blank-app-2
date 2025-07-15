"""
ماژول ابزارهای خروجی گرفتن (Export)
این ماژول شامل توابعی برای تولید گزارش‌ها در فرمت‌های مختلف مانند Excel و PDF است.
"""
import pandas as pd
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def export_to_excel(data: list, columns: list, filename: str):
    """
    داده‌ها را به یک فایل Excel خروجی می‌گیرد.

    :param data: لیستی از دیکشنری‌ها یا اشیاء که هر کدام یک ردیف از داده‌ها هستند.
    :param columns: لیستی از نام ستون‌ها.
    :param filename: نام فایل خروجی (e.g., "report.xlsx").
    """
    # این تابع در آینده تکمیل خواهد شد.
    print(f"Exporting data to {filename}...")
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(filename, index=False)
    print("Export complete.")


def export_to_pdf(data: list, title: str, filename: str):
    """
    داده‌ها را به یک فایل PDF خروجی می‌گیرد.

    :param data: لیستی از رشته‌ها برای نوشتن در PDF.
    :param title: عنوان گزارش.
    :param filename: نام فایل خروجی (e.g., "report.pdf").
    """
    # این تابع در آینده تکمیل خواهد شد.
    print(f"Exporting data to {filename}...")
    # try:
    #     pdfmetrics.registerFont(TTFont('Vazir', 'assets/fonts/Vazir.ttf'))
    # except:
    #     print("Font not found. Using default font.")

    c = canvas.Canvas(filename, pagesize=letter)
    # c.setFont('Vazir', 12) # Use a Persian font
    c.drawString(100, 750, title)

    y = 700
    for line in data:
        c.drawString(100, y, str(line))
        y -= 20

    c.save()
    print("Export complete.")
