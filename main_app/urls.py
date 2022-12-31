from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('workouts/', views.BodypartList.as_view(), name="bodypart_list"),
    path('workouts/<int:pk>/', views.BodypartInfo.as_view(), name="bodypart_info"),
]
