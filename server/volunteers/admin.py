from django.contrib import admin
from .models import Participant, Event, Attendance, Survey, Question,Answer

# Register your models here.
# This will allow the models to be viewed and edited in the Django /admin interface

admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Attendance)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
