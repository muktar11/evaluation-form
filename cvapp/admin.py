# cvapp/admin.py
'''
from django.contrib import admin
from .models import Submission, BookingNotification

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Nationality', 
                    'created_at', 'booked')
    list_filter = ('booked',)

@admin.register(BookingNotification)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('submission', 'booker_name', 'booker_phone', 'created_at')
'''
# cvapp/admin.py
from django.contrib import admin
from .models import Submission, BookingNotification


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'الاسم',               # الاسم
        'الجنسية',             # الجنسية
        'رقم_الترشيح',        # رقم الترشيح
        'العمر',               # العمر
        'اللغة',               # اللغة
        'الحالة_الصحية',       # الحالة الصحية أثناء المقابلة
        'الحالة_النفسية',      # الحالة النفسية
        'المهارات_الأساسية',   # المهارات الأساسية / الوصف الذاتي
        'تم_الحجز',            # تم الحجز
        'تاريخ_الإنشاء',       # تاريخ الإنشاء
    )
    list_filter = ('تم_الحجز',)  # فلتر حسب حالة الحجز


@admin.register(BookingNotification)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'المرشحة',            # المرشحة
        'اسم_الحاجز',         # اسم الحاجز
        'هاتف_الحاجز',        # رقم هاتف الحاجز
        'تاريخ_الإنشاء',      # تاريخ الإنشاء
    )
    list_filter = ('تاريخ_الإنشاء',)  # فلتر حسب تاريخ الإشعار
