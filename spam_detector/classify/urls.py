from django.urls import path
from . import views

urlpatterns = [
    
    path('classify/', views.classify_email, name='classify_email'),
]