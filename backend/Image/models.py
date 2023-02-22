from django.db import models
# Create your models here.
class Image(models.Model) :
    name = models.TextField(default="default")
    uuid_name = models.UUIDField(unique=True) #get image by uuid_name
    email = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Image'
