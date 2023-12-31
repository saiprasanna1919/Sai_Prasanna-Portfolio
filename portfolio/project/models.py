from django.db import models
from django.urls import reverse

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length = 500)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'project_id' : self.id
        })