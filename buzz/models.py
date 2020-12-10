from django.db import models
class Entity(models.Model):
    token=models.CharField(max_length=55)
    time=models.IntegerField()
    tsync_id=models.CharField(max_length=55)


