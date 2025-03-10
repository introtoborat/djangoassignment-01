from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    def __str__(self):
        return self.name 


class EventModel(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField(auto_now=False, auto_now_add=False)
    location=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.name 


class Participant(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=254)
    event=models.ManyToManyField(EventModel, related_name='participants')

    def __str__(self):
        return self.name


