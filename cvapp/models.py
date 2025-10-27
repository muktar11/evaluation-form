# cvapp/models.py
import uuid
from django.db import models
from django.utils import timezone

def video_upload_to(instance, filename):
    return f'videos/{uuid.uuid4()}_{filename}'





class Submission(models.Model):
    """
    Stores the uploaded personal 'template' (video, desc + personal fields).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    health = models.CharField(max_length=200, blank=True, null=True)
    mental_state = models.CharField(max_length=200, blank=True, null=True)
    self_description = models.TextField(blank=True)
    video = models.FileField(upload_to=video_upload_to, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    booked = models.BooleanField(default=False)  # toggles book button disabled in PDF
    booked_at = models.DateTimeField(blank=True, null=True)
    booked_by_name = models.CharField(max_length=200, blank=True, null=True)
    booked_by_phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.id}'

class BookingNotification(models.Model):
    """
    Record of each booking action used for notifications on homepage.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='bookings')
    booker_name = models.CharField(max_length=200)
    booker_phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Booking for {self.submission.name} by {self.booker_name}'
