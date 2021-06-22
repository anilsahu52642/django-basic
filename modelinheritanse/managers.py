from django.db.models import Manager
from django.db import models
class customanil1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
