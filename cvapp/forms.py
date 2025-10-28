'''
from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = [
            'name',          # الاسم
            'nationality',   # الجنسية
            'passport_number', # رقم الجواز
            'age',           # العمر
            'language',      # اللغة
            'health',        # الحالة الصحية
            'mental_state',  # الحالة النفسية
            'self_description', # الوصف الذاتي
            'video'          # الفيديو
        ]
        labels = {
            'name': 'الاسم',
            'nationality': 'الجنسية',
            'passport_number': 'رقم الجواز',
            'age': 'العمر',
            'language': 'اللغة',
            'health': 'الحالة الصحية',
            'mental_state': 'الحالة النفسية',
            'self_description': 'الوصف الذاتي',
            'video': 'الفيديو',
        }


class BookingForm(forms.Form):
    booker_name = forms.CharField(
        max_length=200,
        label='اسم الحاجز'
    )
    booker_phone = forms.CharField(
        max_length=50,
        label='رقم هاتف الحاجز'
    )

'''
from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = [
            'الاسم',
            'الجنسية',
            'رقم_الترشيح',
            'العمر',
            'اللغة',
            'الحالة_الصحية',
            'الحالة_النفسية',
            'المهارات_الأساسية',
            'الفيديو',
        ]
        labels = {
            'الاسم': 'الاسم',
            'الجنسية': 'الجنسية',
            'رقم_الترشيح': 'رقم الترشيح',
            'العمر': 'العمر',
            'اللغة': 'اللغة',
            'الحالة_الصحية': 'الحالة الصحية أثناء المقابلة',
            'الحالة_النفسية': 'الحالة النفسية',
            'المهارات_الأساسية': 'المهارات الأساسية / الوصف الذاتي',
            'الفيديو': 'الفيديو الشخصي',
        }


class BookingForm(forms.Form):
    اسم_الحاجز = forms.CharField(
        max_length=200,
        label='اسم الحاجز'
    )
    هاتف_الحاجز = forms.CharField(
        max_length=50,
        label='رقم هاتف الحاجز'
    )


class BookingForm(forms.Form):
    booker_name = forms.CharField(label="اسم الحاجز", max_length=200)
    booker_phone = forms.CharField(label="هاتف الحاجز", max_length=50)