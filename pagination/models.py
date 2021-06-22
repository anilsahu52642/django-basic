from django.db import models


class blog(models.Model):
    writer=models.CharField(max_length=64)
    content=models.TextField()
