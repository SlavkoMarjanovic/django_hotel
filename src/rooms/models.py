from django.db import models

# Create your models here.
class DetailRoomsView(models.Model):
    name            = models.CharField(max_length=200)
    rooms_type      = models.CharField(max_length=200)
    time_stamp      = models.TimeField(auto_now=True)
    updated         = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.name

