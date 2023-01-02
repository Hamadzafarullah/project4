from .models import Bodypart, Workout
from django.shortcuts import render
from django.views import View  
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class BodypartList(TemplateView):
    template_name = "bodypart_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bodyparts"] = Bodypart.objects.all() 
        return context

class BodypartInfo(DetailView):
    model = Bodypart
    template_name = "bodypart_info.html"

class WorkoutCreate(CreateView):
    model = Workout
    fields = ['name', 'Instructions', 'bodypart']
    template_name = "workout_create.html"
    success_url = "/workouts/"

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['name', 'Instructions', 'bodypart']
    template_name = "workout_update.html"
    success_url = "/workouts/"