from django.db import models
from pytz import timezone
from django.conf import settings
# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    uuid_name = models.TextField(default="", unique=True) #get image by uuid_name
    User = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Image'
