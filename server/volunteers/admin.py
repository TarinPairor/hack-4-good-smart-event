from django.contrib import admin
from .models import AnonymousUser, Event

# Register your models here.
# This will allow the models to be viewed and edited in the Django /admin interface
admin.site.register(AnonymousUser)
admin.site.register(Event)