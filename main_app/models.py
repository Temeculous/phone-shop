from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models
from django.utils import timezone



class Phone(models.Model):
    make = models.CharField(max_length=20)
    serial = models.CharField(max_length=25)
    color = models.CharField(max_length=10)
    condition = models.TextField(max_length=300)
    bought_at = models.DateTimeField(default=timezone.now)

    # It makes it easier for us to read
    def __str__(self):
      return f'{self.make} ({self.id})'