from django.db import models

# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    uuid_name = models.TextField(default="")
    creater
    class Meta:
        db_table = 'Image'