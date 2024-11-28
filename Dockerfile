# از ایمیج پایه استفاده کنید
FROM python:3.9

# تنظیم دایرکتوری کار
WORKDIR /app

# کپی کردن فایل‌های موردنیاز
COPY . /app

# نصب وابستگی‌ها
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# اجرای دستورات اولیه برای پیکربندی پایگاه داده
CMD ["python", "manage.py", "migrate"]

# اجرای سرور جنگو
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
