from django.urls import path

from extra import views


urlpatterns = [
    path('turns-list/', views.turns_list,),
    path('turns-form/', views.create_turns)
]