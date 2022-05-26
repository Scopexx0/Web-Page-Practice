from django.urls import path

from pacients import views


urlpatterns = [
    path('pacient-list/', views.pacient_list),
    path('pacient-form/', views.create_pacient),
]