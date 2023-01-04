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
        context["bodyparts"] = Bodypart.objects.filter(user=self.request.user)
        return context

class BodypartInfo(DetailView):
    model = Bodypart
    template_name = "bodypart_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schedule"] = Schedule.objects.all()
        return context


class WorkoutCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        Instructions = request.POST.get("Instructions")
        bodypart = Bodypart.objects.get(pk=pk)
        Workout.objects.create(name=name, Instructions=Instructions, bodypart=bodypart)
        return redirect('bodypart_info', pk=pk)

     def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkoutCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('bodypart_info', kwargs={'pk': self.object.pk})

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


