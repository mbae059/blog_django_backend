from email.quoprimime import unquote
from django.db import models
from pytz import timezone
from django.conf import settings
# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    uuidName = models.TextField(default="", unique=True) #get image by uuid_name
    userEmail = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Image'
