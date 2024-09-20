from django.db import models


class Data(models.Model):
    file = models.FileField(max_length=100)

