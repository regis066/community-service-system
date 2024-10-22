from django.db import models
from projects.models import Project
from volunteers.models import Volunteer


# Create your models here.
class ServiceHour(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.volunteer.name} - {self.hours} hours"