from datetime import tzinfo
from time import timezone
from django.db import models
from django.forms import TimeField
from django.contrib.auth.models import User
# Create your models here.

class Table(models.Model):
    Capacity=(
			(2, 2),
			(4, 4),
            (6, 6),
			(12, 12),
			)
    seats = models.IntegerField(choices=Capacity,default=2)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    STATUS=(
			('Occupied', 'Occupied'),
			('Empty', 'Empty'),
			)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
