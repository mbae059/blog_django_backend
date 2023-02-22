from django.db import models

# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    uuid_name = models.TextField(default="")
    User = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Image'