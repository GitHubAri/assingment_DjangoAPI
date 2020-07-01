from django.db import models

class Students(models.Model):
    roll_no = models.IntegerField(blank=False, default=1)
    name = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=1)
    marks = models.IntegerField(blank=False, default=0)
