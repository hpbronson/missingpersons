from django.db import models

# Create your models here.
class Table(models.Model):
    date_missing = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    race = models.CharField(max_length=50)