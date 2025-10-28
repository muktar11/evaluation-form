# cvapp/models.py
import uuid
from django.db import models
from django.utils import timezone

def video_upload_to(instance, filename):
    return f'videos/{uuid.uuid4()}_{filename}'



"""
class Submission(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #Name
    Name = models.CharField(max_length=200, blank=True, null=True)
    #Nationality
    Nationality = models.CharField(max_length=50)
    #Referral_Number
    Referral_Number = models.CharField(max_length=100, blank=True, null=True)
    #Age
    Age = models.PositiveIntegerField(blank=True, null=True)
    #Language
    Language = models.CharField(max_length=200, blank=True, null=True)
    #Health_Condition_During_Imprisonment
    Health_Condition_During_Imprisonment = models.CharField(max_length=200, blank=True, null=True)
    #Psychological_Condition
    Psychological_Condition = models.CharField(max_length=200, blank=True, null=True)
    # Basic_skills
    Basic_Skills = models.TextField(blank=True)
    # video
    video = models.FileField(upload_to=video_upload_to, blank=True, null=True)
    # created_at
    created_at = models.DateTimeField(default=timezone.now)
    # booked
    booked = models.BooleanField(default=False)  # toggles book button disabled in PDF
    # booked_at
    booked_at = models.DateTimeField(blank=True, null=True)
    # booked_by_name
    booked_by_name = models.CharField(max_length=200, blank=True, null=True)
    # booked_by_phone
    booked_by_phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.id}'

class BookingNotification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='bookings')
    booker_name = models.CharField(max_length=200)
    booker_phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Booking for {self.submission.name} by {self.booker_name}'
"""



class Submission(models.Model):
    """
    نموذج تخزين البيانات الشخصية (الفيديو، الوصف، والمعلومات الشخصية)
    """

    المعرف = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    الاسم = models.CharField(max_length=200, blank=True, null=True)
    الجنسية = models.CharField(max_length=50)
    رقم_الترشيح = models.CharField(max_length=100, blank=True, null=True)
    العمر = models.PositiveIntegerField(blank=True, null=True)
    اللغة = models.CharField(max_length=200, blank=True, null=True)
    الحالة_الصحية = models.CharField(max_length=200, blank=True, null=True)
    الحالة_النفسية = models.CharField(max_length=200, blank=True, null=True)
    المهارات_الأساسية = models.TextField(blank=True)
    الفيديو = models.FileField(upload_to=video_upload_to, blank=True, null=True)
    تاريخ_الإنشاء = models.DateTimeField(default=timezone.now)
    تم_الحجز = models.BooleanField(default=False)
    تاريخ_الحجز = models.DateTimeField(blank=True, null=True)
    اسم_الحاجز = models.CharField(max_length=200, blank=True, null=True)
    هاتف_الحاجز = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return f'{self.الاسم} - {self.معرف}'


class BookingNotification(models.Model):
    """
    سجل كل عملية حجز تُعرض في صفحة الإشعارات الرئيسية
    """

    المعرف = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    المرشحة = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='الحجوزات')
    اسم_الحاجز = models.CharField(max_length=200, blank=True, null=True)
    هاتف_الحاجز = models.CharField(max_length=50, blank=True, null=True)
    تاريخ_الإنشاء = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'حجز لـ {self.المرشحة.الاسم} بواسطة {self.اسم_الحاجز}'