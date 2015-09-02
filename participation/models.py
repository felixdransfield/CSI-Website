from django.db import models
from django.utils import timezone


# models your models here.
class Participation(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField('Age')
    #sex = models.MultipleChoiceField
    email = models.EmailField(help_text='A valid email address, please.')
    phone = models.IntegerField('Telephone Number')
    date = models.DateField('', default=timezone.now, blank=True)