from django.db import models

# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    day = models.IntegerField()
    uuid_name = models.TextField(default="")

    class Meta:
        db_table = 'Image'