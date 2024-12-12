from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('do/', views.do, name='do'),
    path('internship_apply_4_weeks/', views.internship_apply_4_weeks, name='internship_apply_4_weeks'),
    path('internship_apply_6_weeks/', views.internship_apply_6_weeks, name='internship_apply_6_weeks'),
    path('internship_apply_8_weeks/', views.internship_apply_8_weeks, name='internship_apply_8_weeks'),
    path('portfolio/', views.portfolio, name='portfolio'),
]