# cvapp/urls.py
from django.urls import path
from . import views

app_name = 'cvapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_submission, name='create_submission'),
    path('submission/<uuid:pk>/', views.submission_detail, name='submission_detail'),
    path('submission/<uuid:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('submission/<uuid:pk>/book/', views.book_submission, name='book_submission'),
    path('submission/<uuid:pk>/preview/', views.preview_submission, name='preview_submission'),

    
]
