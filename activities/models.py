from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class EventModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name 


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    event = models.ManyToManyField(EventModel, related_name='participants')

    def __str__(self):
        return self.name

class Event_register(models.Model):
    event_name=models.ManyToManyField("EventModel", related_name='all_events')
    participants_name=models.ManyToManyField("Participant", related_name='all_participants')


@receiver(post_save, sender=Participant)
def notify_participant_on_creation(sender, instance, created, **kwargs):
    if created:
        events = instance.event.all() # connecting all events registered by participants
        event_details = "\n".join([f"- {event.name} on {event.date} at {event.time}" for event in events])

        send_mail(
            "Registration Confirmation",
            f"Dear {instance.name},\n\nYou have successfully registered for the following event(s):\n\n{event_details}\n\nSee you there!",
            "saifulibarat@gmail.com",  
            [instance.email],  
            fail_silently=False,  
        )
