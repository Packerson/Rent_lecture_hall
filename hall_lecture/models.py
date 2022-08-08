from django.db import models


# Create your models here.
class Hall(models.Model):
    hall_name = models.CharField(max_length=255, unique=True)
    hall_capacity = models.IntegerField()
    projector = models.BooleanField()


class Booked(models.Model):
    booked_date = models.DateField()
    id_lecture_hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)

    class Meta:
        unique_together = ['booked_date', 'id_lecture_hall']
