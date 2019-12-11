from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('teacher_logout', views.teach_logout, name='teach_logout'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('addstu', views.addstu, name='addstu'),
    path('allstudent', views.allstudent, name="allstudent"),
    path('enterClass/<str:classno>', views.enterClass, name="enterClass")
]
