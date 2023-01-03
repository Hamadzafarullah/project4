from .models import Bodypart, Workout, Schedule
from django.shortcuts import render
from django.views import View  
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect 

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

# class WorkoutCreate(CreateView):
#     model = Workout
#     fields = ['name', 'Instructions', 'bodypart']
#     template_name = "workout_create.html"
#     success_url = "/workouts/"

class WorkoutCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        Instructions = request.POST.get("Instructions")
        bodypart = Bodypart.objects.get(pk=pk)
        Workout.objects.create(name=name, Instructions=Instructions, bodypart=bodypart)
        return redirect('bodypart_info', pk=pk)

class ScheduleList(TemplateView):
    template_name = 'schedule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schedule"] = Schedule.objects.all()
        return context



# class WorkoutUpdate(UpdateView):
#     model = Workout
#     fields = ['name', 'Instructions', 'bodypart']
#     template_name = "workout_update.html"
#     success_url = "/workouts/"

# class WorkoutDelete(DeleteView):
#     def delete(self, request, pk):
#     model = Workout
#     template_name = "workout_delete_confirmation.html"
#     success_url = "/workouts/"

# class WorkoutDelete(View):

#     def delete(self, request, pk):
#         name= request.GET.get("name")
#         length = request.GET.get("Instructions")
#         bodypart = Bodypart.objects.get(pk=pk)
#         Workout.objects.remove(name=name, Instructions=Instructions, bodypart=bodypart)
#         return redirect('bodypart_info', pk=pk)
