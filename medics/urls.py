from django.urls import path

from medics import views


urlpatterns = [
    path('medic-list/', views.medic_list, name='medics'),
    path('medic-form/', views.create_medic),
    path('search/', views.search, name='search'),
]