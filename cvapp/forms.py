# cvapp/forms.py
from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['name', 'phone', 'passport_number', 'age', 'self_description', 'video']

class BookingForm(forms.Form):
    booker_name = forms.CharField(max_length=200)
    booker_phone = forms.CharField(max_length=50)
