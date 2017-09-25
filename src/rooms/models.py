from django.db import models

# Create your models here.
class DetailRoomsView(models.Model):
    rooms_type = models.CharField(max_length=200)
