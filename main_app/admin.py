from django.contrib import admin
from .models import Bodypart 
from .models import Workout
from .models import Schedule


admin.site.register(Bodypart) 
admin.site.register(Workout) 
admin.site.register(Schedule) 