from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models
from django.utils import timezone



class Phone(models.Model):
    make = models.CharField(max_length=20)
    serial = models.CharField(max_length=25)
    color = models.CharField(max_length=10)
    condition = models.TextField(max_length=300)
    bought_at = models.DateTimeField(default=timezone.now, blank=True,null=True )

    # It makes it easier for us to read
    def __str__(self):
      return f'{self.make} ({self.id})'
    

    def get_absolute_url(self):
       return reverse('detail', kwargs={'phone_id': self.id})
