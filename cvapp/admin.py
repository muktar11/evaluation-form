# cvapp/admin.py
from django.contrib import admin
from .models import Submission, BookingNotification

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'booked')
    list_filter = ('booked',)

@admin.register(BookingNotification)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('submission', 'booker_name', 'booker_phone', 'created_at')
