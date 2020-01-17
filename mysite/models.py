from django.db import models

class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True