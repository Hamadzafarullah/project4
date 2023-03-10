from .models import Bodypart, Workout, Schedule
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class BodypartList(TemplateView):
    template_name = "bodypart_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bodyparts"] = Bodypart.objects.filter(user=self.request.user)
        return context

class BodypartInfo(DetailView):
    model = Bodypart
    template_name = "bodypart_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schedule"] = Schedule.objects.all()
        return context


class WorkoutCreate(CreateView):

    def post(self, request, pk):
        name = request.POST.get("name")
        Instructions = request.POST.get("Instructions")
        bodypart = Bodypart.objects.get(pk=pk)
        Workout.objects.create(name=name, Instructions=Instructions, bodypart=bodypart)
        return redirect('bodypart_info', pk=pk)


@method_decorator(login_required, name='dispatch')
class ScheduleList(TemplateView):
    template_name = 'schedule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schedule"] = Schedule.objects.all()
        return context


class ScheduleWorkoutAssoc(View):

    def get(self, request, pk, workout_pk):

        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Schedule.objects.get(pk=pk).workouts.remove(workout_pk)
        if assoc == "add":
            Schedule.objects.get(pk=pk).workouts.add(workout_pk)
        return redirect('/schedules')



class Signup(View):
   
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
   
   
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("bodypart_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
