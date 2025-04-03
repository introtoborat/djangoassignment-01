from django.contrib import admin
from activities.models import Category, EventModel, Participant

# Register your models here.
#admin.site.register(Category)
admin.site.register(EventModel)
admin.site.register(Participant)