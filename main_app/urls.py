from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('workouts/', views.BodypartList.as_view(), name="bodypart_list"),
    path('workouts/<int:pk>/', views.BodypartInfo.as_view(), name="bodypart_info"),
    path('workouts/addworkout/<int:pk>/', views.WorkoutCreate.as_view(), name="workout_create"),
    path('schedules/',views.ScheduleList.as_view(), name='schedule_list'),
]